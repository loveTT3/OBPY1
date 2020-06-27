



def fun(f):
    def inner():
        print('新加的功能')
        ret = f()
        return ret
    return inner


@fun
def index():
    print('欢迎光临')

# index = fun(index)
index()