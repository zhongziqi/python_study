# -*- coding: UTF-8 -*-
 # 求1+2!+3!+...+20!的和
n = 0
s = 0
t = 1
for n in range(1,21):
    t *= n
    s += t
print '1! + 2! + 3! + ... + 20! = {0}'.format(s)
