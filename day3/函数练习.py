# 命名关键字参数
# def foo(x,y,*args,a=1,b,**kwargs):
#     print(x,y)
#     print(args)
#     print(a)
#     print(b)
#     print(kwargs)
#
# foo(1,2,3,4,5,b=3,c=4,d=5)
# 1.计算字符串中【数字】，【字母】，【空格】以及【其他】的个数
# def check_str(msg):
#     res = {
#         'num': 0,
#         'string': 0,
#         'space': 0,
#         'other': 0
#     }
#     for s in msg:
#         if s.isdigit():
#             res['num'] += 1
#         elif s.isalpha():
#             res['string'] += 1
#         elif s.isspace():
#             res['space'] += 1
#
#         else:
#             res['other'] += 1
#     return res
#
#
# res = check_str('hello everyone :i am jiangfan ,age 18')
# print(res)

#2.写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者
# def fun(seq):
#     if len(seq) > 2:
#         seq=seq[0:2]
#     return seq
# print(fun(['happy','everyday',11,33,44]))


#3.写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。
# def func1(seq):
#     return seq[::2]
# print(func1(['haa','lalala','xixixx',12,34,5,56,78,9]))

#4.写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def func2(dic):
    d = {}
    for k,v in dic.items():
        if len(v) > 2:
            d[k] = v[0:2]
    return d
print(func2(dic = {"k1": "v1v1", "k2": [11,22,33,44]}))