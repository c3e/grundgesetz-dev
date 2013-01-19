#!/usr/bin/env python
# -*- coding: utf-8 -*-

from codecs import open
import os
# from glob import glob

from difflib import SequenceMatcher, Differ

import regex

class Token:

    punct_re = regex.compile(ur"^\p{P}+$")

    def __init__(self, tok, typ="w", from_v=0, to_v=None):
        self.tok = tok
        self.is_typ()
        self.from_v = from_v
        self.to_v = to_v

    def is_typ(self):
        if self.punct_re.match(self.tok):
            self.typ = "p"
        else:
            self.typ = "w"
        

    def __repr__(self):
        ret = u"<{} |{}| {} <= v'".format(self.typ, self.tok,
                self.from_v)
        if self.to_v is not None:
            ret += self.to_v
        ret += ">"
        return ret.encode("utf-8")

SRC_DIR = u"../src"
versionen = xrange(2,4)
fn_s = [
            u"107.md",
            # u"002.md",
    ]

tok_re = regex.compile(ur'(?iu)([\d\w()]+|[\p{P}]+)')

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


f_toks = []
for v in versionen:
    for fn in fn_s:
        f_toks.append(tokenise_file(fn, v))

print f_toks

tok_ranges = compare_toks(f_toks[0], f_toks[1])

# - gemeinsame Tokens: to_version setzen
# - unterschiedliche Tokens:
#   - nur in i: from_v = i
#   - nur in i-a: to_v = i-1

# - Graphisieren



