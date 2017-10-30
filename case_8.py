# -*- coding: UTF-8 -*-
for i in range(1,10):
    print
    for y in range(1,i+1):
         print "%d*%d=%d" % (i, y, i*y),
# 打印九九乘法口诀表
# 其中第一个print为将第一次的循环放在一处，如果没有第二个print 的话该打印就会竖直排列，
# 第二个print的作用是水平排列
