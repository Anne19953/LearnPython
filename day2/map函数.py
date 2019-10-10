num_l = [1,2,34,123,123,12]
def map_test(func, array):
    ret = []
    for i in array:
        res = func(i)
        ret.append(res)
    return ret


print(map_test(lambda x: x + 1, num_l))

###################使用map()效果一样，num_l需要是可迭代对象
res = (map(lambda x: x + 1, num_l))
print(list(res))


mes = 'annehded'
h = list(map(lambda x:x.upper(),mes))
print(h)