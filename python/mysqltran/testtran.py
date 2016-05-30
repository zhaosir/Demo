#! /usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import MySQLdb
import MySQLdb.cursors
import ipdb
#ipdb.set_trace()


def test():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='zhaozijian@123', db='test', cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute('select * from u_test')
    ret0 = cur.fetchall()
    print 'test.ret0', ret0
    cur.execute('select * from u_test where name=%s', ('jim', ))
    ret1 = cur.fetchall()
    print 'test.ret1', ret1

def test1():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='zhaozijian@123', db='test', cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute('select * from u_test')
    ret0 = cur.fetchall()
    print 'test1.ret0', ret0
    cur.execute('select * from u_test where name=%s', ('jim', ))
    ret1 = cur.fetchall()
    print 'test1.ret1', ret1
    test()
    cur.execute('insert into u_test (name, u_age) values (%s, %s)', ('jim', '10'))
    cur.execute('select * from u_test where name=%s', ('jim', ))
    ret2 = cur.fetchall()
    print 'test1.ret2', ret2
    test()
    conn.commit()
    cur.execute('select * from u_test where name=%s', ('jim', ))
    ret3 = cur.fetchall()
    print 'test1.ret3', ret3
    test()



def test_update():
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='zhaozijian@123', db='test', cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    cur.execute('select * from u_test')
    ret0 = cur.fetchall()
    print 'test_update.ret0', ret0
    cur.execute('update u_test set u_age=%s where name=%s', (30, 'jim'))
    cur.execute('select * from u_test where name=%s', ('jim', ))
    ret1 = cur.fetchall()
    print 'test_update.ret1', ret1
    test()
    conn.commit()
    test()

def test_update_1():
    ipdb.set_trace()
    conn = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='zhaozijian@123', db='test', cursorclass=MySQLdb.cursors.DictCursor)
    cur = conn.cursor()
    conn1 = MySQLdb.connect(host='127.0.0.1', port=3306, user='root', passwd='zhaozijian@123', db='test', cursorclass=MySQLdb.cursors.DictCursor)
    cur1 = conn1.cursor()
    cur.execute('select * from u_test')
    ret0 = cur.fetchall()
    print 'test_update.ret0', ret0
    cur.execute('update u_test set u_age=%s where name=%s', (30, 'jim'))
    cur1.execute('update u_test set u_age=%s where name=%s', (40, 'jim'))
    cur.execute('select * from u_test where name=%s', ('jim', ))
    ret1 = cur.fetchall()
    print 'test_update.ret1', ret1
    cur1.execute('select * from u_test where name=%s', ('jim', ))
    ret2 = cur1.fetchall()
    print 'test_update.ret2', ret2

    test()
    conn.commit()
    conn1.commit()
    test()

test_update_1()



