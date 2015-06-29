#! /usr/bin/env python
# -*- coding:utf-8 -*-

import upyun

try:
	up = upyun.UpYun(bucket='ktvdarenresource', username='zhaozijian', password='leishi@2012', timeout=30, endpoint=upyun.ED_AUTO)
	print up.getinfo('/test103.jpg')
except Exception,e:
	print e
