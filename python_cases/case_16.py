# -*- coding: utf-8 -*-
# 引入时间模块
import datetime
# strftime 里面的%Y 代表2017 如果换成y 则打印出来17
# print(datetime.date.today().strftime('%y-%m-%d'))
print(datetime.date.today().strftime('%Y-%m-%d'))
# 将某个时间转成某个时间格式
special_date = datetime.date(1949,10,1);
# strftime 这个函数可以理解为可以将某个时间段转为特定的时间格式的函数
print(special_date.strftime('people republic of china was found in:%Y-%m-%d'))
# 至于这个timedelta的用法权且放一下，仅仅知道在做日期相减或者相加时，用它来处理加数
special_date = special_date + datetime.timedelta(days=1)

print(special_date.strftime('%Y/%m/%d'))

# 日期替换
special_date = special_date.replace(special_date.year + 1)

print(special_date.strftime('%Y/%m/%d'))
