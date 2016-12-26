#! /usr/bin/env python
# -*- coding:utf-8 -*-


import multiprocessing, time  
import multiprocessing.pool
import threading

def run(): 
    i = 0;  
    try:
        while i<1000:  
            print 'running';  
            time.sleep(1);  
            i += 1;  
    except:
        pass

def add(v):
    print 'v=%s\n' % v
    time.sleep(10)
    return v * 2

_pool = multiprocessing.pool.ThreadPool(3)
#_pool = multiprocessing.pool.Pool(1)

if __name__ == '__main__':  
#    ret = _pool.map(run, [1])
#    _pool.apply_async(run)
#    _pool.close()
#    _pool.join()
#    p = multiprocessing.Process(target=run);  
#    p.start();  

    t = threading.Thread(target=run, args=())
#    t.setDaemon(True)
    t.start()
    print 'p.start() end'
#    p.join();  
#    print p.pid;  
    print 'master gone';  
    i = 0
    while i < 10:
        print 'main runing'
        i += 1
        time.sleep(1)
