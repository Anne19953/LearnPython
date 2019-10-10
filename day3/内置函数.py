# #1.all()全不为0才为真
# print(all([0,1,2]))
# #2.any()只要有一个不为0就为真
# print(any([1,0,4]))
# #3.ascii()--------->不知道怎样用的
# print(ascii(['asd']))
# #bin()十进制转2进制
# print(bin(2))
# #bytes()字符串不可以修改，列表可以修改
# a = bytes('abcde',encoding='utf-8')
# #a[0] = 200  #-------->不可以修改
# print(a)
# b = bytearray('abcde',encoding='utf-8')
# b[0] = 99  #------>原先为a 97 现在为 c 99
# print(b)
#查找ascii对应的字符
print(chr(87))
#查找字符对应的ascii
print(ord('c'))
#查找内置方法
a = []
b = ''
print(dir(a))  #列表的方法
print(dir(b))  #字符串方法



#匿名函数
res = filter(lambda n:n>5,range(10))
for i in res:
    print(i)

