#usr/bin/python3
#coding:utf-8
#coding= gpk2312
#!#元组定义以及书写
tub1 = ('hello','world','python3','python3.7');
tub2 = (1,2,3,4,5,6,7,);
tub3 = "a","b","c","d";
type(tub2)
print(tub1)
print(tub3)
#元组使用下标访问
#元组使用下标访问
#元组使用下标访问
tub4 = ('中国我爱你','google','1997',2000)
tub5 = (1,2,3,4,5,6,7,8,9)

print(tub4[0:3])
print(tub5[1:5])
print(tub3[0])

#修改元组
#修改元组
tup1 = (12,34.54)
tup2 = ('abc','xyz')
#修改元组非法操作
#tup1[0]=100
tup3=tup1+tup2
print(tup3)
#删除元祖
tup = ('google','crown',1997,2000)
print(tup)
del tup

print("删除厚的元祖:")
tup = ('google','crown',1997,2000)
print(tup)
#元祖运算符
#计算元祖个数
#计算元祖个数

len(tup)
#元祖的链接
num=tup+tub1+tub3
print("输出元组连接")
print(num)
#元祖的复制
print("输出元组复制")
print(num*2)
#判断元祖是否存在这个元素
#判断元祖是否存在这个元素
print("判断元素是否存在元组中")
print("判断元组中的元素是否存在:"'google' in num)
#迭代输出
print("迭代输出元组")
for x in num:
    print(x)
#元组截取和反向读取，元组索引
L = ('goolge', "Taobao","return")
print("元组:%s")
print("输出截取")
print(L(2))
print("反向截取")
print(L(-2))
#元组内置函数
#元组内置函数
#元组内置函数
print("输出元组中最大的和最小的
")
tuple1 = (1,2,3,4,78,34,22,)
print(max(tuple1))
print(min(tuple1))
