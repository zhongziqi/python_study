# -*- coding: UTF-8 -*-
for i in range(1,5):
	for y in range(1,5):
		for k in range(1,5):
			if(i!=y)and(i!=k)and(y!=k):
				print i,y,k
				# 这里有一点需要注意的是range里面的范围是含头不含尾的

				# 计算1，2，3，4组成的三位数可能出现的情况有哪些，而且不能重复
