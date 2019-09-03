#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from panflute import toJSONFilter, run_filter, Str, Para, debug, convert_text, ListContainer


def getRubyTag(string):
    newstring=string
    # |単語《読み》 generate <ruby>単語<rt>よみ</rt></ruby>
    rubyset = [re.compile("[\|｜]([^\|｜|^《（\(].+?)《([^《》].+?)》"),
               re.compile("[\|｜]([^\|｜|^《（\(].+?)（([^（）].+?)）"),
               re.compile("[\|｜]([^\|｜|^《（\(].+?)\(([^\(\)].+?)\)"),
               re.compile("([々〇〻\u2E80-\u2FDF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F][\uDC00-\uDFFF]+)《(.+?)》"),
               re.compile("([々〇〻\u2E80-\u2FDF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F][\uDC00-\uDFFF]+)（([ぁ-ん|ァ-ヶ|ー|＝|・]+?)）"),
               re.compile("([々〇〻\u2E80-\u2FDF\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]|[\uD840-\uD87F][\uDC00-\uDFFF]+)\(([ぁ-ん|ァ-ヶ|ー|＝|・]+?)\)")]

    # |《単語》 just generate 《単語》, presercing bracket
    non_ruby_bracket=[{"regex": re.compile("[\|｜]《(.+?)》"),"left": "《","right": "》"},
                      {"regex": re.compile("[\|｜]（(.+?)）"),"left": "（","right": "）"},
                      {"regex": re.compile("[\|｜]\((.+?)\)"),"left": r"(","right": r")"}]


    for rubyrule in rubyset:
        newstring = re.sub(rubyrule, "<ruby>\\1<rt>\\2</rt></ruby>",newstring)

    for noruby in non_ruby_bracket:
        newstring = re.sub(noruby["regex"], noruby["left"]+"\\1"+noruby["right"],newstring)

    return newstring


def rubify(elem, doc):
    if type(elem) == Str:
        rubied_text = getRubyTag(elem.text)
        rubied_para = convert_text(rubied_text)
        rubied_elems=[]
        if isinstance(rubied_para, ListContainer):
            for item in rubied_para.content:
                rubied_elems.append(item)
            for i, item in enumerate(rubied_elems, elem.index+1):
                elem.parent.content.insert(i,item)
            return []


def main(doc=None):
    return run_filter(rubify, doc=doc)
    
if __name__ == "__main__":
    main()