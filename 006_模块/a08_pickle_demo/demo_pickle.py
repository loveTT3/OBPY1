# pickle模块是将Python所有的数据结构以及对象等转化成bytes类型，然后还可以反序列化还原回去。
import pickle


# dumps loads
dic = {'k1':'v1','k2':'v2'}
str_dic = pickle.dumps(dic)   
print(str_dic)  # b'\x80\x04\x95\x19\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x02k1\x94\x8c\x02v1\x94\x8c\x02k2\x94\x8c\x02v2\x94u.'
dic2 = pickle.loads(str_dic)
print(dic2)    # {'k1': 'v1', 'k2': 'v2'}

# 序列化对象
def func():
    print(666)
ret = pickle.dumps(func)
print(ret,type(ret))
f1 = pickle.loads(ret)
f1()


# dump  load
dic = {(1,2):'嘤嘤嘤',1:True,'set':[1,2,3]}

with open('pick序列化',mode = 'wb') as ff:
    pickle.dump(dic,ff)


# pickle序列化存储多个数据到一个文件中
dic1 = {'name':'oldboy1'}
dic2 = {'name':'oldboy2'}
dic3 = {'name':'oldboy3'}

f2 = open('pick多数据',mode='wb')
pickle.dump(dic1,f2)
pickle.dump(dic2,f2)
pickle.dump(dic3,f2)
f2.close()

f = open('pick多数据',mode='rb')
while True:
    try:
        print(pickle.load(f))
    except EOFError:
        break
f.close()