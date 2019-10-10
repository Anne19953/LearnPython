import json
path = '/Users/anne/Desktop/workspace/data.txt'
#将数据转为jsong格式
records = [json.loads(line) for line in open(path)]
# print(records[0])
#对时区进行统计
# time_zones = [rec['tz'] for rec in records if 'tz' in rec]
#对时区计数
# def get_counts(sequences):
#     counts = {}
#     for x in sequences:
#         if x in counts:
#             counts[x] +=1
#         else:
#             counts[x] = 1
#     return counts
# counts =get_counts(time_zones)
# print(counts)
#
# print(counts['America/New_York'])
# print(len(time_zones))

#求前10位的时区及其计数值
# def top_counts(count_dict,n=10):
#     value_key_pairs = [(count,tz) for tz,count in count_dict.items()]
#     value_key_pairs.sort()
#     return value_key_pairs[-n:]
#
# print(top_counts(counts))


###############使用pandas
from pandas import  DataFrame,Series
import pandas as pd;import numpy as np
import matplotlib.pyplot as plt
frame = DataFrame(records)
# print(frame)
#展示出现的前十个时区
# print(frame['tz'][:10])
#显示时区出现次数最多的10个
# tz_counts = frame['tz'].value_counts()
# print(tz_counts[:10])

#将缺失值用Missin代替，空字符用unknown代替
# clean_tz = frame['tz'].fillna('Missing')
# clean_tz[clean_tz == ''] = 'Unknown'
# tz_counts = clean_tz.value_counts()
# print(tz_counts[:10])
#在ipython环境下可以以图标形式展现
# tz_counts[:10].plot(kind='barh',rot=0)


#统计a字段
#将a字段的信息按空格分裂，保留第一个信息，dropna()缺少的部分遗弃
results = Series([x.split()[0] for x in frame.a.dropna()])
# results= frame['a'].value_counts()

#显示前5个
# print(results[:5])
#显示浏览器被使用最高的8个
# print(results.value_counts()[:8])
#将agent缺失的移除
cframe = frame[frame.a.notnull()]
#将浏览器分为Windows和not windows
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print(operating_system[:5])
#根据时区和新的系统进行分组
by_tz_os = cframe.groupby(['tz',operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)
# print(agg_counts[:10])

#选取最常出现的时区
indexer = agg_counts.sum(1).argsort()
print(indexer[:10])
#按照顺序截取最后10行
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)

# count_subset.plot(kind='barh',stacked=True)
# plt.show()

#按照总计为1来显示
normed_subset = count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)
plt.show()

