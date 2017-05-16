import functools

def log(text = ''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
            if text != '':
                print('%s %s():' %(text,func.__name__))
                func(*args,**kw)
            else:
                print('%s():' %func.__name__)
                func(*args,**kw)
        return wrapper
    return decorator

@log()   #这种办法无法去掉log后面的括号
def f1():
    print('I am Func1\n')

@log('execute')
def f2():
    print('I am Func222222\n')

if __name__ == '__main__':
    f1()
    f2()

