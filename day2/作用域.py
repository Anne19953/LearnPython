# def test1():
#     print('in the test1')
# def test():
#     print('in the test')
#     return test1
#
# res = test()
# print(res())






# name = "Alex"
#
#
# def change_name():
#     name = "Alex2"
#
#     def change_name2():
#         name = "Alex3"
#         print("第3层打印", name)
#
#     change_name2()  # 调用内层函数
#     print("第2层打印", name)
#
#
# change_name()
# print("最外层打印", name)



# name = 'alex'
# def foo():
#     name = 'lhf'
#     def bar():
#         print(name)
#     return bar
# func = foo()
# func()





name = 'alex'
def foo():
    name = 'lhf'
    def bar():
        name = 'anne'
        def tt():
            print(name)
        return tt
    return bar
func = foo()
func()()