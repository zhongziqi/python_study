# -*- coding : utf-8 -*-
year = int(raw_input('year:'))
month = int(raw_input('month:'))
day = int(raw_input('day:'))
# months = (0,31,59,90,120,151,181,212,243,273,304,334)
# 上下两者都是正确的方式  上为元组 元素不可修改
months = [0,31,59,90,120,151,181,212,243,273,304,334]
if(0<month<=12):
	sum = months[month-1]
else:
	print 'something went wrong'
sum+=day
leap=0
if(year%400==0) or (year%4==0) and (year%100!=0):
	leap = 1
if(leap == 1) and (month>2):
	sum+=1;
print sum

# 输入某年某月某日，判断这一天是这一年的第几天？
