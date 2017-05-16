import functools

def reminder(func):
    def wrapper(*args,**kw):
        print('Begin Call\n')
        func(*args,**kw)
        print('End Call\n')
    return wrapper

@reminder
def fun():
    print('I am a Function\n')

if __name__ == '__main__':
    fun()
