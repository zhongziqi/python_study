# -*- coding:utf-8 -*-
score = int(raw_input('plear input your score:'))
if(score>=90):
    grade = 'A'
elif(score>=60):
    grade = 'B'
else:
    grade = 'C'
print 'your score: %d it belongs %s' % (score,grade)
