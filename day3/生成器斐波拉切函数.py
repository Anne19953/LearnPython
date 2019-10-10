# def fib(max):
#     n,a,b = 0,0,1
#     while n < max:
#         print(b)
#         a,b = b,a+b     #t = (a,a+b) a=t[0] b = t[1]
#         n = n+1
#     return 'done'
# fib(8)


#generator()
#将print改成yield
def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b     #t = (a,a+b) a=t[0] b = t[1]
        n = n+1
    return 'done'

g = fib(6)
print(g)


#打印
print('----------打印结果')
for i in fib(6):
    print(i)

#
print('---------捕获返回值')
while True:
    try:
        x = next(g)
        print('g:',x)
    except StopIteration as e:
        print('Generate return value:',e.value)
        break

