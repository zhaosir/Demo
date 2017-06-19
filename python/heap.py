#! /usr/bin/env python
# -*- coding:utf-8 -*-


class MinHeap:  
    def __init__(self):  
        self.list = [0]  
        self.size = 0  
  
    def __str__(self) :  
        return " ".join(str(v) for v in self.list[1:])  
          
    def up(self, i) :  
        while i / 2 > 0 :  
            if self.list[i] < self.list[i / 2] :  
                self.list[i], self.list[i / 2] = self.list[i / 2], self.list[i]  
            i = i / 2  
  
    def insert(self, k) :  
        self.list.append(k)  
        self.size += 1  
        self.up(self.size)  
  
    def minchild(self, i) :  
        if i * 2 + 1 > self.size :  
            return i * 2  
        else :  
            if self.list[i * 2] < self.list[i * 2 + 1] :  
                return i * 2  
            else :  
                return i * 2 + 1  
  
    def down(self, i) :  
        while i * 2 <= self.size :  
            minc = self.minchild(i)  
            if self.list[i] > self.list[minc] :  
                self.list[i], self.list[minc] = self.list[minc], self.list[i]  
            i = minc  
  
    def build(self, src_list) :  
        i = len(src_list) / 2  
        self.size = len(src_list)  
        self.list.extend(src_list)  
        while i > 0 :  
            self.down(i)  
            i -= 1  
  
#src_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]  
src_list = [9,8,5,3,1,2]  
  
mh = MinHeap()  
mh.build(src_list)  
print mh  
