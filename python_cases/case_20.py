# -*- coding:utf-8 -*-
# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
tour = []
height = []

hei = 100.0 # 起始高度
tim = 10 # 次数

for i in range(1, tim + 1):
    # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
    if i == 1:
        tour.append(hei)
    else:
        tour.append(2*hei)
    hei /= 2
    height.append(hei)
# python2.6开始，新增了一种格式化字符串的函数str.format()
print('total_height:tour = {0}'.format(sum(tour)))
# height[-1]代表列表中倒数后一位数数字
print('No.10:height = {0}'.format(height[-1]))
