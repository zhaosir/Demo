#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
import thread,threading

def timer(no,interval):
    cnt = 0
    while cnt < 10:
        print 'thread:%d time:%s \n' % (no,time.ctime())
        time.sleep(interval)
        cnt += 1
    thread.exit_thread()


def test():
    thread.start_new_thread(timer,(1,1))
    thread.start_new_thread(timer,(2,2))


if __name__ == '__main__':
    th = threading.Thread(target=timer,args=(2,2))
    th.setDaemon(True)
    th.start()
#    test()
#    time.sleep(20)
