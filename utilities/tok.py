#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Tokenizes and compares two versions

from codecs import open
import os
from collections import OrderedDict
# from glob import glob

from difflib import SequenceMatcher

import regex

from bs4 import BeautifulSoup

numbered_re = regex.compile(ur'^(?:(?:\d+|[XVI]+)[a-z]\.)')



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
        ret = self.eq_typ(self, other)
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


class HierItem:
    u'''versioned hierarchical item in the German Grundgesetz

    special case: if the text is only "[aufgehoben]", the item has been
    repealed'''

    def is_repealed(self):
        if len(self.children) == 1 and \
            self.children[0].p == u"[aufgehoben]":
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
        ("tag", ur'(?V1)<[^>]*?>'),
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


f_toks = []

version_trees = {}

for v in versionen:
    for fn in fn_s:
        print "V: ", v
        soup = soupify_file(fn, v)
        version_trees = [Section(a) for a in soup("h1")]

        # f_toks.append(tokenise_file(fn, v))


# print f_toks
#
# tok_ranges = compare_toks(f_toks[0], f_toks[1])

# - gemeinsame Tokens: to_version setzen
# - unterschiedliche Tokens:
#   - nur in i: from_v = i
#   - nur in i-a: to_v = i-1

# - Graphisieren



