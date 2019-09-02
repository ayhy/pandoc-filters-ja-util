#!/usr/bin/env python
# -*- coding: utf-8 -*-

#- Pandoc filter to convert dash ― into horizontal line ─,
#which allows continuous line in double dash――.


from panflute import run_filter, Str
import re

def dash(elem, doc):
    if type(elem) == Str:
        elem.text = elem.text.replace("―","─")
        return elem


def main(doc=None):
    return run_filter(dash, doc=doc)

    
if __name__ == "__main__":
    main()