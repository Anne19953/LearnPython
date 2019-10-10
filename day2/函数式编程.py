######高介函数
# 把函数当成参数传给另一个函数
# def foo(n):
#     print(n)
#
#
# def bar(name):
#     print('my name is %s' % name)


# foo(bar)  # 传入的是bar的地址
# foo(bar())  #报错
# foo(bar('alex'))  # n=bar('alrx') = None


# 返回值中包含函数
# def bar():
#     print('from bar')
#
#
# def foo():
#     print('from foo')
#     return bar
#
#
# n = foo()
# n()

# 返回值是自己
# def handle():
#     print('from handle')
#     return handle
# h = handle()
# h()





