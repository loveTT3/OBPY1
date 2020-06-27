from core import src

# 装饰器
def auth(f):
    def inner(*args,**kwargs):
        if status_dicts['status']:
            f(*args,**kwargs)
        else:
            login()
            f(*args,**kwargs)
    return inner