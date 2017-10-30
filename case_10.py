# -*- coding: UTF-8 -*-
# python 获取当前时间
# 睡眠一秒然后再打印
import time
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
time.sleep(1)
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
