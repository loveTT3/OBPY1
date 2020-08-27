from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.AutoField(primary_key=True) #如果表里面没有写主键，表里面会自动生成一个自增主键字段，叫做id字段，orm要求每个表里面必须要写一个主键
    title=models.CharField(max_length=32)  #和varchar(32)是一样的，32个字符
    state=models.BooleanField()
    pub_date=models.DateField() #必须存这种格式"2018-12-12"
    price=models.DecimalField(max_digits=8,decimal_places=2) #max_digits最大位数，decimal_places小数部分占多少位
    publish=models.CharField(max_length=32)
class Meta:  # 必须要写这个类
    db_table = 'Book'  # 指定表名