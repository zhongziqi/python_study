# -*- coding: UTF-8 -*-

def output(s,l):
    if l==0:
       return
    print (s[l-1])
    print l
    output(s,l-1)

s = raw_input('Input a string:')
l = len(s)
output(s,l)
