# def foo():
#     print('foo')
# def bar():
#     print('bar')
# dic={
#     'foo':foo,
#     'bar':bar,
# }
# while True:
#     choice = input('>>:').strip()
#     if choice in dic:
#         dic[choice]()


#函数作用域在定义阶段就固定了
# x=1
# def f1():
#     def f2():
#         print(x)
#     return f2
# x=100
# def f3(func):
#     x=2
#     func()
# x=10000
# f3(f1())


#闭包
# def counter():
#     n = 0
#
#     def incr():
#         nonlocal n
#         x = n
#         n += 1
#         return x
#
#     return incr
#
#
# c = counter()
# print(c())
# print(c())
# print(c())
# print(c.__closure__[0].cell_contents)  # 查看闭包的元素


from urllib.request import urlopen


def index(url):
    def get():
        return urlopen(url).read()

    return get


baidu = index('http://www.baidu.com')
print(baidu().decode('utf-8'))