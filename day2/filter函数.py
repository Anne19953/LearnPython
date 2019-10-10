################fliter()
movie_people = ['s_anne','s_xiaofan','s_song','s_dahong','yanfei']
# def s_show(n):
#     return n.startswith('s')
#--------------->lambda n:n.startswith('s)


# def fliter_test(func,array):
#     ret = []
#     for item in array:
#         if not func(item):
#             ret.append(item)
#     return ret
# print(fliter_test(s_show,movie_people))

#########使用lambda
def fliter_test(func,array):
    ret = []
    for item in array:
        if not func(item):
            ret.append(item)
    return ret
print(fliter_test(lambda n:n.startswith('s'),movie_people))#


#---------filter函数
movie_people = ['s_anne','s_xiaofan','s_song','s_dahong','yanfei']
res = filter(lambda n:not n.startswith('s'),movie_people)
print(list(map(lambda n:not n.startswith('s'),movie_people)))   #[False, False, False, False, True]
print(res)   # <filter object at 0x1098b6c18>
print(list(res))