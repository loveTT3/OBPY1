# 反射： 用字符串类型的名字 操作这个名字对应的函数实例变量绑定方法各种方法

name = 'alex'
age = 123
n = input('>>>')
if n == 'name': print(name)
elif n == 'age':print(age)


# 明知道变量的字符串数据类型的名字  想直接调用它 但是调用不到
# 使用场景

# 1.反射对象的 实例变量
# 2.反射类的 静态变量 绑定方法 其他方法
# 3.模块中的所有变量