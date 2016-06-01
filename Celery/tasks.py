#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
from celery import Celery
import uuid

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def sendmail(mail):
#    print('sending mail to %s...' % mail['to'])
#    time.sleep(2.0)
    raise Exception('err')
    print 'data len', len(mail)
    print('mail sent.')


if __name__ == '__main__':
    for k in xrange(100000):
        ps = []
        for i in xrange(1):
            ps.append({
                'deviceid': str(uuid.uuid1()),
                'playload': {
                    'sound': '123sdfsd',
                    'title': '你好你好你好',
                    'content': '山东发顺丰撒萨法术飞洒发萨芬水电费',
                    'url': 'http://sdddddddddddddddddddddddddddddddddddddddd/sdfas/sdf'
                }
            })
#        print 'data ok'
        a = time.time()
        ret = sendmail.delay(ps)
#        print time.time() - a
    print ret
