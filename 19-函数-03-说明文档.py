"""
思考：定义⼀个函数后，程序员如何书写程序能够快速提示这个函数的作⽤？
答：注释
思考：如果代码多，我们是不是需要在很多代码中找到这个函数定义的位置才能看到注释？如果想更⽅
便的查看函数的作⽤怎么办？
答：函数的说明⽂档
"""

# 函数的说明⽂档也叫函数的⽂档说明。

# 语法
# 定义函数的说明⽂档
'''
def 函数名(参数):
    """ 说明⽂档的位置 """
    代码
    ......
'''
# 查看函数的说明⽂档
"""help(函数名)"""


def sum_num(a, b):
    """ 求和函数 """
    return a + b


help(sum_num)
