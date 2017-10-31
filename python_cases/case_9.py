# -*- coding: UTF-8 -*-
# 等三秒打印我爱你
import time
obj = {'a':'i like you','b':'i love you'}
# print dict.values(obj)
# print dict.keys(obj)
# print dict.values(obj)
for key,value in dict.items(obj):
    print value
    time.sleep(3)
