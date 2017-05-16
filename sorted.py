L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
	return t[0]

def by_score(t):
    return t[1]

L2 = sorted(L,key=by_name)
print(L2)
L3 = sorted(L,key=by_name,reverse = True)
print(L3)
'''
sorted利用的是key指定函数的 返回值 从小到大排序
'''
