# def test01():
#     msg = 'hello The little green frog'
#     print(msg)
#
#
# def test02():
#     msg = 'hello WuDaLang'
#     print(msg)
#     return msg
#
#
# t1 = test01()
#
# t2 = test02()
#
#
# print('from test01 return is [%s]' % t1)
# #
# print('from test02 return is [%s]' % t2)

#
# def test01():
#     pass
#
#
# def test02():
#     return 0
#
#
# def test03():
#     return 0, 10, 'hello', ['alex', 'lb'], {'WuDaLang': 'lb'}
#
#
# t1 = test01()
# t2 = test02()
# t3 = test03()
#
# print('from test01 return is [%s]: ' % type(t1), t1)
# print('from test02 return is [%s]: ' % type(t2), t2)
# print('from test03 return is [%s]: ' % type(t3), t3)


# def test(x,*args):
#     print(x)
#     print(args)
#
# test(1,['x','y','z'])
# test(1,*['x','y','z'])


# name = "a"
# def a():
#     name = "b"
#     def b():
#         global name
#         name = "c"
#     b()
#     print(name)
# print(name)
# a()
# print(name)


# 问路
# person_list = ['anne', 'song', 'jack', 'yanfei', 'dahong']


# def ask_way(person_list):
#     if len(person_list) == 0:
#         return "没人知道"
#     person = person_list.pop(0)
#     if person == 'yanfei':
#         return '%s说：我知道，跟我来！' % person
#     print('hi [%s],敢问路在何方' % person)
#     print(('%s 回答道：我不知道，我帮你问问%s...') % (person, person_list))
#     res = ask_way(person_list)
#     return res


# res = ask_way(person_list)
# print(res)


# s = ['h','e','l','l','o']
# #1
# r = s[::-1]
# print(r)
# #2
#
# r = (''.join(reversed(s)))
# print(list(r))
# #3


name='lhf'

def change_name():
    print('我的名字',name)

change_name()


def change_name():
    name='帅了一笔'
    print('我的名字',name)

change_name()
print(name)



def change_name():
    global name
    name='帅了一笔'
    print('我的名字',name)

change_name()
print(name)