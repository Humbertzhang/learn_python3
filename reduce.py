#coding:utf-8
from functools import reduce
def str2float(s):
    dotindex = s[::-1].index('.')
    n = 10**-dotindex
    return n*reduce(lambda x,y:x*10+y,[int(a) for a in s if a is not '.'])

print('str2float(\'123.456\') =', str2float('123.456'))

'''
1,逆序方法 list[::-1]
2,list 的 index()方法
3,列表生成式:  [int(a) for a in list if a is not '.']

