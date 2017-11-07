# -*- coding: utf-8 -*-
# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
Tn = 0
Sn = []
# n 为循环的个数
n = int(raw_input('n = '))
# a 为数字
a = int(raw_input('a = '))
for count in range(n):
    Tn = Tn + a
    a = a * 10
    Sn.append(Tn)
    # append 方法向列表的尾部添加一个新的元素。
    # extend() 方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中
    print Sn
# lambda 是一个简写的函数
# reduce里的函数必须接收两个参数，sn为列表，计算的先后顺序是：先将列表的前两个相加，（如果列表的长度大于2）则将相加的结果继续加上第三个参数
Sn = reduce(lambda x,y : x + y,Sn)
print "THE FINAL RESULT IS:",Sn
