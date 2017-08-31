import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s:' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@log('begin')
def call():
    print('2017-8-30')

# @log('end')


# call.__name__
call()
