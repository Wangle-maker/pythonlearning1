# 了解引⽤
# 在python中，值是靠引⽤来传递来的。

# 我们可以⽤ id() id() 来判断两个变量是否为同⼀个值的引⽤。 我们可以将id值理解为那块内存的地址标识。

# 1. int类型
a = 1
b = a
print(b)  # 1
print(id(a))  # 140708464157520
print(id(b))  # 140708464157520
a = 2
print(b)  # 1,说明int类型为不可变类型
print(id(a))  # 140708464157552，此时得到是的数据2的内存地址
print(id(b))  # 140708464157520

# 2. 列表
aa = [10, 20]
bb = aa
print(id(aa))  # 2325297783432
print(id(bb))  # 2325297783432
aa.append(30)
print(bb)  # [10, 20, 30], 列表为可变类型
print(id(aa))  # 2325297783432
print(id(bb))  # 2325297783432

# 引⽤当做实参
def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))


# int：计算前后id值不同
b = 100
test1(b)
# 列表：计算前后id值相同
c = [11, 22]
test1(c)
