#1
# num_l = [1,2,34,56]
# # res = 0
# for num in num_l:
#     res+=num
# print(res)


#2
# num_l = [1,2,34,56]
# def reduce_test(array):
#     res = 0
#     for num in array:
#         res += num
#     return res
#
# print(reduce_test(num_l))

#3
# num_l = [1,2,3,5]
# def multi(x,y):
#     return  x*y
#-------------------------->lambda x,y:x*y
# def reduce_test(func,array):
#     res = array.pop(0)
#     for item in array:
#         res =func(res,item)
#     return res
# h = reduce_test(multi,num_l)
# print(h)

#4  指定一个初始值
# num_l = [1,2,3,5]
# def reduce_test(func,array,init=None):
#     if init == None:
#         res = array.pop(0)
#     else:
#         res = init
#     for item in array:
#         res =func(res,item)
#     return res
# h = reduce_test(lambda x,y:x*y,num_l)
# print(h)

#5 reduce()
# from functools import reduce
# num_l = [1,2,3,5]
# print(reduce(lambda x,y:x*y,num_l,1))


#--------------------》总结
# name_dic = [
#     {'name':'anne','age':24},
#     {'name':'song','age':27},
#     {'name':'fei','age':44},
# ]
#
# res=(filter(lambda x:x['age']>30,name_dic))
# print()
# for i in res:
#     print(i)

####reduce()
# from functools import reduce
# print(reduce(lambda x,y:x+y,range(100),100))
# print(reduce(lambda x,y:x+y,range(1,101)))


####map()
name = ['anne','song','fei']
res = map(lambda x:'super_'+x,name)
print(list(res))

