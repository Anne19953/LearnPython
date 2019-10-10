# calc = lambda n:n**n
# print(calc(10))


l = [3, 2, 100, 999, 213, 1111, 31121, 333]
print(max(l))
dic = {'k1': 10, 'k2': 100, 'k3': 30}
print(dic[max(dic,key=lambda k:dic[k])])
