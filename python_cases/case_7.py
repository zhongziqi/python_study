# -*- coding: UTF-8 -*-
# 需要申明一点就是  python2   处理的情况和python有所不同
# 将一个列表的数据复制到另一个列表
# 方法一：
a = [1,2,3]
b = a[:]
print b;

# 方法二：
l = [1,2,3,4,5,6,7]
b = []
for i in range(len(l)):
    b.append(l[i])
print b
