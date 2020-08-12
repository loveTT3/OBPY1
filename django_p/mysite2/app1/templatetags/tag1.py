from django import template

# 这个是自定义过滤器
register = template.Library()  #register的名字是固定的,不可改变
# 没有参数
@register.filter
def xx(v1):
    aaa = 'wobunimade'
    return v1+aaa

# 有一个参数
@register.filter
def xxxx(v1,v2):
    return v1 + v2


# 这个是自定义标签
# 可以多个参数
@register.simple_tag
def tagg1(v1):
    return v1 * 2

@register.simple_tag
def tagg2():
    return '嘤嘤嘤'

@register.simple_tag
def tagg3(v1,v2,v3):
    return v1 + v2 + v3   