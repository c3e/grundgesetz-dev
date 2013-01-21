#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Tokenizes and compares two versions

from codecs import open
import os
import sys
try:
    from collections import OrderedDict
except ImportError:
    from ordereddict import OrderedDict
# from glob import glob

from difflib import SequenceMatcher

import regex

from bs4 import BeautifulSoup, element

numbered_re = regex.compile(ur'^(?:(?:\d+|[XVI]+)[a-z]\.)')


def is_numbered(s):
    return numbered_re.search(s)


class Item:
    u'''versioned item in the German Grundgesetz

    special case: if the text is only "[aufgehoben]", the item has been
    repealed'''

    def __init__(self, tok, from_v=0, to_v=None):
        self.tok = tok
        self.from_v = from_v
        self.to_v = to_v
        self.children = []  # ordered list of children

    def eq_typ(self, other):
        ret = True
        if unicode(self.tok) != unicode(other.tok):
            ret = False
        return ret

    def eq_deep(self, other):
        ret = self.eq_typ(other)
        if ret:
            if len(self.children) > 0:
                if len(self.children) != len(other.children):
                    ret = False
                else:
                    ret = all(c[0].eq_deep(c[1]) \
                            for c in zip(self.children, other.children))
        return ret

    def __repr__(self):
        ret = u"<{} |{}| {} <= v'".format(self.__class__.__name__, self.tok,
                self.from_v)
        if self.to_v is not None:
            ret += self.to_v
        ret += ">"
        return ret.encode("utf-8")


class HierItem(Item):
    u'''versioned hierarchical item in the German Grundgesetz

    special case: if the text is only "[aufgehoben]", the item has been
    repealed'''

    def is_repealed(self):
        if len(self.children) == 1 and \
            self.children[0].p.text == u"[aufgehoben]":
                return True
        return False

    def get_number(self):
        return numbered_re.search(self.tok)


class Preamble(HierItem):
    u'''Just an item; introduced for having nice semantic names'''
    typ_name = u"Präambel"


class Section(HierItem):
    u'''Just an item; introduced for having nice semantic names'''
    typ_name = u"Abschnitt"


class Article(HierItem):
    u'''Just an item; introduced for having nice semantic names'''
    typ_name = u"Artikel"


class WRVArticle(HierItem):
    u'''Just an item; introduced for having nice semantic names

    (article of the Weimarian Constitution from 1919 still valid today)
    '''


class Paragraph(HierItem):
    u'''Just an item; introduced for having nice semantic names'''
    typ_name = u"Absatz"


class Token(Item):

    u'''versioned token

    a token is ± a word or punctuation.

    TODO: add pre- (opening parentheses, quotation marks etc.) and
    postspacing (others) attributes to punctuation

    '''

    punct_re = regex.compile(ur"^\p{P}+$")

    def __init__(self, tok, typ="w", from_v=0, to_v=None):
        self.tok = tok
        self.is_typ()
        self.from_v = from_v
        self.to_v = to_v

    def __eq__(self, other):
        return self.eq_typ(other) and self.typ == other.typ

    def is_typ(self):
        if self.punct_re.match(self.tok):
            self.typ = "p"
        else:
            self.typ = "w"

    def __repr__(self):
        ret = u"<Tok {} |{}| {} <= v'".format(self.typ, self.tok,
                self.from_v)
        if self.to_v is not None:
            ret += self.to_v
        ret += ">"
        return ret.encode("utf-8")


SRC_DIR = u"../src"
versionen = xrange(2, 4)
fn_s = [u"GG.html"]

# Replace by hash: typ => re
tok_re = regex.compile(ur'(?iu)([\d\w()]+|[\p{P}]+)')

# ordered so that tags are not "eaten" by punctuation tokens
tok_tok = OrderedDict([
        ("tag_open", ur'(?V1)<[^/][^>]*?>'),
        ("tag_close", ur'(?V1)</[^>]*?>'),
        ("word", ur'(?V1)[\d\w()]+'),
        ("punct_pre", ur'(?V1)[\p{Ps}\p{Pi}]+'),
        ("punct_post", ur'(?V1)[\p{P}&&\P{Ps}&&\p{Pi}]+'),
    ])

tok_re = u"(?:" + u"|".join(tok_tok.values()) + u")"


def compare_toks(t1, t2):
    sm = SequenceMatcher(None, [t.tok for t in t1], [t.tok for t in t2])
    return sm.get_matching_blocks()


def tokenise_file(fn, v):
    fn_akt = os.path.join(SRC_DIR, unicode(v), fn)
    print fn_akt
    with open(fn_akt, encoding="utf-8") as f:
        toks = [Token(m.group())
                for line in f.readlines()
                for m in tok_re.finditer(unicode(line))]

    return toks


def get_version_dir(v):
    ret = SRC_DIR
    if v > 0:
        ret = os.path.join(ret, unicode(v))
    return ret


def soupify_file(fn, v):
    fn_akt = os.path.join(get_version_dir(v), fn)
    print fn_akt
    return BeautifulSoup(open(fn_akt, encoding="utf-8"))


tag_hierarchy = [
     "h1",
     "h2",
     # "ol", # not necessary as this is already a tree
]


def arborify(soup):
    u'''semanticise markup: document tree from tag soup'''
    cur_el = soup.h1
    tag_stack = []
    div_stack = [BeautifulSoup()]
    # loop over elements and build div-tree
    while cur_el is not None:  # Warning: cur_el may be non-element!
        next_el = cur_el.next_sibling
        if type(cur_el) == element.Tag and cur_el.name in tag_hierarchy:
            if tag_stack:
                hier = tag_hierarchy.index(tag_stack[-1].name)
            else:  # trick für initial element
                hier = -1
            cur_hier = tag_hierarchy.index(cur_el.name)
            if tag_stack:
                if hier >= cur_hier:
                    # could we have a tag_stack == ["h1", "ol"]?
                    # should not, but we can take care of it:
                    while tag_stack and tag_hierarchy.index(tag_stack[-1].name) >= cur_hier:
                        tag_stack.pop()
                        div_stack.pop()
            tag_stack.append(cur_el)
            div_stack.append(soup.new_tag("div", level=cur_hier))
            div_stack[-2].append(div_stack[-1])
            div_stack[-1].insert_after("\n")
        if div_stack:
            div_stack[-1].append(cur_el)
        else:
            sys.stderr.write("Dangling text!? {}".format(unicode(cur_el)))
        cur_el = next_el
    return div_stack[0]

f_toks = []

version_trees = {}

def objectify(soup, v):
    sections = []
    for sec in soup("div", level=0):
        sec_tree = Section(sec.h1, from_v = v, to_v = v)
        for art in sec("div", level=1):
            art_tree = Article(art.h2)
            if art.ol:
                for para in art.ol("li"):
                    para.name = "para"
                    art_tree.children.append(unicode(para.contents))
            sec_tree.append(art_tree)

            sec_tree.children.


for v in versionen:
    for fn in fn_s:
        print "V: ", v
        soup = soupify_file(fn, v)
        semantic_soup = arborify(soup)

        # with open("GG_%02d.html"%v, "w") as gg:
        #     gg.write(unicode(arborify(soup)))

        # f_toks.append(tokenise_file(fn, v))


# print f_toks
#
# tok_ranges = compare_toks(f_toks[0], f_toks[1])

# - gemeinsame Tokens: to_version setzen
# - unterschiedliche Tokens:
#   - nur in i: from_v = i
#   - nur in i-a: to_v = i-1

# - Graphisieren



