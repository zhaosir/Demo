#! /usr/bin/env python
# -*- coding:utf-8 -*-

data = range(8)
total = len(data)
line = 3
rowcount = total / line

if total % line >0:
    rowcount = rowcount + 1

print rowcount

#res = {}
for i in range(rowcount):
    res = []
    idx_1 = i
    for j in range(line):
        idx_2 = j + 1
        idx = (idx_1 * line)  + idx_2
#        print idx_1,idx_2
        if idx < total:
            print idx
    
