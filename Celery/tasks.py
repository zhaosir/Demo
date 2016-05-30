#! /usr/bin/env python
# -*- coding:utf-8 -*-

import time
from celery import Celery

celery = Celery('tasks', broker='redis://localhost:6379/0')

@celery.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')


if __name__ == '__main__':
    ret = sendmail.delay(dict(to='celery@python.org'))
    print ret
