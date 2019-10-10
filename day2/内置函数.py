
##########
# name = 'anne'
# print(hash(name))
# name = 'sb'
# print(hash(name))
#
# print(bin(10))#---->10进制转2进制
# print(hex(12))#----->10进制转16进制
# print(otc(12))#------->10进制转8进制


#zip(拉链一一对应)
# print(zip(('a','b','c'),(1,2,3)))
# print(list(zip(('a','b','c'),(1,2,3))))
# dic = {'name':'jiangfan','age':24,'gender':'female'}
# print(zip(dic.keys(),dic.values()))
# print(list(zip(dic.keys(),dic.values())))

#max
# l = [
#     (5,'e'),
#     (1,'b'),
#     (3,'a'),
#     (4,'d'),
# ]
# print(max(l))


# ll = ['a10','b2','c10',1111] #类型不同不能比较
# ll = ['a10','b2','c10']
# print(max(ll))

# age_dic = {'anne':24,'song':26,'fei':44}
#默认比较的是字典的key
# print(max(age_dic))
# print(max(age_dic.values()))
#

#将key和value交换位置，再进行比较
# ll = list(zip(age_dic.values(),age_dic.keys()))
# print(max(ll))


#找出年纪最大的，并显示所有信息
# dic = [{'name':'anne','age':14},{'name':'yanfei','age':44},
#        {'name':'song','age':28}]
# print(max(dic,key=lambda dic:dic['age']))

##排序

age_dic = {'fei':44,'anne':24,'song':26,}
#默认key排序
print(sorted(age_dic))
#只要人名
print(sorted(age_dic,key=lambda key:age_dic[key]))
#既要人名也要年纪
print(sorted(zip(age_dic.values(),age_dic.keys())))
# people = [{'name':'anne','age':14},{'name':'yanfei','age':44},
#        {'name':'song','age':28}]
# print(sorted(people))
