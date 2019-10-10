# % +str
# tpl = 'i am %s' % 'alex'
# print(tpl)
# % +tuple
# tpl1 = 'i am %s, i am %s' %('alex',18)
# print(tpl1)
# % +dic
# tpl2 = 'i am %(name)s age %(age)d' %{'name':'anne','age':18}
# print(tpl2)
# tpl3= 'percent %.2f %%' %99.234
# print(tpl3)
# tpl4 = 'i am %(tt).2f %%' % {'tt': 123.45678}
# print(tpl4)


#####################format()

# tpl = 'i am {}, age {}, {}'.format('seven',18,'anne')
# print(tpl)

# tpl1 = 'i am {}, age {}, {}'.format(*['seven',18,'anne'])
# print(tpl1)

# tpl2 = "i am {0}, age {1}, really {0}".format("seven", 18)
# print(tpl2)


# tpl3 = "i am {name}, age {age}, really {name}".format(**{'name':"seven", 'age':18})
# print(tpl3)


# tpl4 = "i am {0[0]}, age {0[1]}, really {1[2]}".format([1, 2, 3], [11, 22, 33])
# print(tpl4)



# tpl5 = "i am {:s}, age {:d}, money {:f}".format('ssss', 18, 888.33)
# print(tpl5)

tpl6 = "i am {:s}, age {:d}".format(*["seven", 18])
print(tpl6)

