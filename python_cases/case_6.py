# -*- coding: UTF-8 -*-
def fib(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b
        # 上面这种操作被叫为赋值运算，先计算等于好右边的然后再相等
    return a
# 输出了第10个斐波那契数列
print fib(10)
# 总结：斐波那契数列指的是符合0，1，1，2，3，5，8，13，21，34。。。的数列


# def calc(n):
#     a,b=1,1
#     for i in range(n-1):
#         a,b=b,a+b
#     return a
# print calc(10)
