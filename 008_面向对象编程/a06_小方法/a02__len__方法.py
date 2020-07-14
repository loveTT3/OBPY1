# __len__  

class Cls:
    def __init__(self,name):
        self.name = name
        self.students = []
    def __len__(self):
        return len(self.students)


py22 = Cls('PY22')
py22.students.append('aa')
print(len(py22.students))
print(len(py22))  # 想调用 必须写__len__函数
