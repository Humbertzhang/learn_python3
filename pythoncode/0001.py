'''
知识：１，随机数　２，不可重复的类型
'''
from random import *

numset = set()
word = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'


while(len(numset) <=199):
    s = ''
    while(len(s) < 20):
        ranum1 = randint(0,1)
        if ranum1 == 0:
            s += word[randint(0,25)]
        elif ranum1 == 1:
            s += num[randint(0,9)]

    numset = numset|{s}

for i,item in enumerate(numset):
    print('%d : %s' % (i+1,item))
