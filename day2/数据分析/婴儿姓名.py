import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
names1880 = pd.read_csv('/Users/anne/Desktop/workspace/data_analysis/names/yob1880.txt',names=['name','sex','births'])
#以sex分组小计表示该年度的birth总计：
# names1880.groupby('sex').births.sum()
#将所有数据都组装到一个DataFrame里面
years = range(1880,2011)
pieces = []
columns = ['name','sex','births']
for year in years:
        path = '/Users/anne/Desktop/workspace/data_analysis/names/yob%d.txt' %year
        frame = pd.read_csv(path,names=columns)

        frame['year'] = year
        pieces.append(frame)

names = pd.concat(pieces,ignore_index=True)
# print(names)

#统计每年出生的男孩女孩各有多少
# total_births = names.pivot_table('births',index='year',columns='sex',aggfunc=sum)
# print(total_births.tail())

# total_births.plot(title='Total births by sex and year')
# plt.show()

#统计叫某名字的婴儿所占比例
def add_prop(group):
    births = group.births
    group['prop'] = births / births.sum()
    return group
names = names.groupby(['year','sex']).apply(add_prop)
# print(names)
#检查所有比例之和是否为1
print(np.allclose(names.groupby(['year','sex']).prop.sum(),1))

#取组合的前1000个名字
def get_top1000(group):
    return group.sort_values(by='births',ascending=False)[:1000]
########################有错误
grouped = names.groupby()

top1000 = grouped.apply(get_top1000)

# print(top1000)

#g根据性别将前1000个数据分成男孩，女孩
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births',index='year',columns='name',aggfunc=sum)
print(total_births)
# subset = total_births[['John','Harry','Mary','Marilyn']]
# subset.plot(subplots=True,grid=False,title='Number of births per year')
# plt.show()
table = top1000.pivot_table('prop',index='year',columns='sex',aggfunc=sum)
table.plot(title='Sum of tsble1000.prop by year and sex',yticks=np.linspace(0,1.2,13),xticks=range(1880,2020,10))
