class Person:
    def __init__(self,name,sex,job,hp,weapon,ad):
        self.name = name
        self.sex = sex
        self.job = job
        self.level = 0
        self.hp = hp
        self.weapon = weapon
        self.ad = ad


bob = Person('BOB','男','teacher',1000,'peaper',1)
print(bob)
print(bob.__dict__)
bob.aaa = 111
print(bob.__dict__)
del bob.ad
print(bob.__dict__)