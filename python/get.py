#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import httplib

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2369.0 Safari/537.36'
}
conn = httplib.HTTPConnection(host='www.ktvdaren.com')
conn.request(method='GET',url='/sysres/htmltemplet/valiemail_templet.html',headers=headers)
response = conn.getresponse()
temp = response.read()
print type(temp)
print temp
