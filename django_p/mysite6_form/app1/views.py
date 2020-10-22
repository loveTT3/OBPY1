import re  
# 应用库的顺序
# 标准库、第三方库、django里面的内容，中间应有换行

from django.shortcuts import render,HttpResponse,redirect
from django import forms
from django.forms import widgets
from django.forms import fields
from django.core.validators import RegexValidator
from django.core.validators import ValidationError

# Create your views here.

def test1(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        
        if form_obj.is_valid():
            print(form_obj.cleaned_data)# 获取post提交的内容，校验完之后才有这个值
            return HttpResponse("注册成功")
    
    return render(request, "test.html", {"form_obj": form_obj})

# 校验函数
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')  #自定义验证规则的时候，如果不符合你的规则，需要自己发起错误


# 创建Form类时，主要涉及到 【字段】 和 【插件】，字段用于对用户请求数据的验证，插件用于自动生成HTML;
class RegForm(forms.Form):
    # 字段名为前端标签的name
    name = forms.CharField(  
        min_length=3, 
        max_length=11,
        required=True, # 必填，默认true
        strip=True, #是否移除输入左右的空白
        label = '用户名',  
        initial='请输入你的名字',  # 输入框默认值
        help_text='3-11位',
        # 正则校验器
        # validators=[
        #     RegexValidator(r'^[0-9]+$', '请输入数字'), 
        #     RegexValidator(r'^159[0-9]+$', '数字必须以159开头')
        #     ],
        #   
        # validators=[
        #     mobile_validate,],

        error_messages={
            "required":"不能为空",
            "invalid":"格式错误",
            "min_length":"用户名最短3位"
        },
    )
    # 密码 
    pwd = forms.CharField(
        min_length = 4,
        label="密码",
        # 密码字段默认在前端输入数据错误的时候，点击提交之后，默认是不保存的原来数据，
        # 但是可以通过这个render_value=True让这个字段在前端保留用户输入的数据
        widget=forms.PasswordInput(attrs={'class':'c1'},render_value=True),
        error_messages={
            "required":"不能为空",
            "invalid":"格式错误",
            "min_length":"密码最短4位"
        },
        )
    
    # 局部钩子  命名：clean_字段
    def clean_name(self):
        value = self.cleaned_data['name']
        if '傻逼' in value:
            raise ValidationError('含有敏感词"傻逼"')
        else:
            return value

    # 全局钩子
    def clean(self):
        value = self.cleaned_data
        n1 = value['name']
        n2 = value['pwd']
        if  n1 == n2:
            return value
        else:
            self.add_error('pwd','密码不等于用户名')
            raise ValidationError('yyy')

    # radioSelect  单radio值为字符串
    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        help_text='111',
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )

    # 单选select  
    hobby = forms.fields.ChoiceField(  #注意，单选框用的是ChoiceField，并且里面的插件是Select，不然验证的时候会报错， Select a valid choice的错误。
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )

    # 多选select
    hobby1 = forms.fields.MultipleChoiceField( #多选框的时候用MultipleChoiceField，并且里面的插件用的是SelectMultiple，不然验证的时候会报错。
        choices=((1, "篮球1"), (2, "足球1"), (3, "双色球1"), ),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )

    # 单选checkbox
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        choices=(
            ('True',1),
            ('False',0),
        ),
        initial="1",
        widget=forms.widgets.CheckboxInput()
    )

    # 多选checkbox
    hobby2 = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )


    # date类型
    date = forms.DateField(
        widget=widgets.TextInput(attrs={'type':'date'})
        
        )  #必须指定type，不然不能渲染成选择时间的input框

