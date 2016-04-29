#! /usr/bin/env python
# -*- coding:utf-8 -*-


import xml.etree.ElementTree as ET
import json
xml_str = u'<?xml version="1.0" encoding="utf-8"?><user><name>jim</name><job><comp>joy</comp><work><time>2015</time><date>10:00</date></work></job><age>20</age></user>'
xml_str = u'<?xml version="1.0" encoding="utf-8"?><user></user>'
def parseXml2Dict(xml_data):
    u'''简单实现，不支持多级元素，不支持属性,一般不直接调用
    '''
    j_data = {}
    try:
        root = ET.fromstring(xml_data)
        res = parseChild(root)
        print json.dumps(res)
    except Exception, ex:
            print ex
#-#        error('解析xml失败\nxml=%s', repr(xml_data), exc_info=True)
    return j_data

def parseChild(el):
    res = {}
    _temp_child = el.getchildren()
    if len(_temp_child) <=0 :
        res[el.tag] = el.text
        return res
    for _child in el.getchildren():
        _temp_child = _child.getchildren()
        if len(_temp_child) > 0:
            res[_child.tag] = parseChild(_child)
        else:
            res[_child.tag] = _child.text 
    return res

parseXml2Dict(xml_str)
