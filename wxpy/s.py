#! /usr/bin/env python
# -*- coding:utf-8 -*-


from wxpy import * 
import time

bot = Bot()
friends = bot.friends()
for f in friends:
    print f

my_friend = bot.friends().search(u'赵子剑')[0]

# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    print msg
    return 'received: {} ({}) url={}'.format(msg.text, msg.type, msg.url)

print("ending")
while True:
    time.sleep(1)
embed()

