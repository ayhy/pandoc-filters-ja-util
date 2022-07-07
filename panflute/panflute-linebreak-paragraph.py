#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pandoc filter to split paragraph with contains linebreak 
into seperate paragraphs. 
Intended use: CJK paragraph writing with +hard_line_breaks extension

the the filter will turn sample into result:
sample = Doc(Para(Str("test"), LineBreak, Str("test2"), Space, Str("test3")))
result = Doc(Para(Str(Test)), Para(Str("test2"), Space, Str("test3")))
"""


import panflute as pf

def break_newpara(elem, doc):
    if type(elem) == pf.Para:
        splitParas=[]
        singleParaElems=[]
        needs_to_be_split=False
        for segment in elem.content:
                if isinstance(segment, pf.LineBreak):
                    needs_to_be_split=True

        if needs_to_be_split:
            for segment in elem.content:
                if isinstance(segment, pf.LineBreak):
                    splitParas.append(pf.Para(*singleParaElems))
                    singleParaElems=[]
                else:
                    singleParaElems.append(segment)
            splitParas.append(pf.Para(*singleParaElems))
#            pf.debug("Before--------------------")
#            pf.debug(elem.parent.content)
#            pf.debug("Before--------------------")
            for i, item in enumerate(splitParas, elem.index+1):
                elem.parent.content.insert(i, item)
#            pf.debug("Afer--------------------")
#            pf.debug(elem.parent.content)
#            pf.debug("Afer--------------------")
            #Delete the original Para
            return []
        else:
#            pf.debug("no softbreak or linebreak found")
#            pf.debug(elem)
            return elem

if __name__ == "__main__":
    pf.toJSONFilter(break_newpara)