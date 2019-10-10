#高阶函数
# 特点 1.把一个函数名当成实参传给另一个函数(在不修改源代码的前提下，为其他函数添加
# 功能)
#2.返回值是一个函数名（不修改函数的调用方式）
import time
# def bar():
#     time.sleep(3)
#     print("inr the bar")
#
# def test1(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print("the func run time is %s "%(stop_time-start_time))
#
# test1(bar)


######################第二种情况
def bar():
    time.sleep(3)
    print("inr the bar")

def test2(func):
    print(func)
    return func

bar = test2(bar)
bar()

