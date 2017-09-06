import time

def clock(func):

    #装饰器所装饰的函数所接受的变量会传递给里面的函数. 

    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8f] %s(%s) -> %r' % (elapsed, name, arg_str, result))
        return result

    return clocked
