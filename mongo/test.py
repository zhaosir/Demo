#! /usr/bin/env python
# -*- coding:utf-8 -*-

# https://pypi.python.org/pypi/pymongo/#downloads
import pymongo

conn = pymongo.Connection("192.168.2.202",27017)
db = conn.ec_medlinker_data #连接库
db.ec_product_uv.save({'p_id':1,'uv': 0, 'uv_date': '2016-07-09'})
