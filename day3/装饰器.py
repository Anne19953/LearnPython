#本质是函数（装饰其他函数）为其他函数添加附加功能
#原则 1：不能修改被修饰函数的源代码 2:不能修改被修饰函数的调用方式
# 装饰器==>高阶函数+嵌套函数
#嵌套函数格式
#def timer():
    # def deco():
    #     pass



import time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print("the func run time is %s" %(stop_time-start_time))
    return deco
@timer    # test1 = timer(test1)   返回值是deco 那么test1 = deco
def test1():
    time.sleep(3)
    print('in the test1')
@timer    #test2 = timer(test2)
def test2(name,age):
    time.sleep(1)
    print('test2:',name,age)

test1() #--------->相当于deco()
test2('anne',25)
