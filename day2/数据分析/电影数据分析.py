import pandas as pd
unames = ['user_id','gender','age','occupation','zip']
users = pd.read_csv('/Users/anne/Desktop/workspace/data_analysis/movies/users.dat',sep='::',header=None,names=unames)

rnames = ['user_id','movie_id','rating','timestamp']
ratings = pd.read_csv('/Users/anne/Desktop/workspace/data_analysis/movies/rating.dat',sep='::',header=None,names=rnames)

mnames = ['movie_id','title','genres']
movies = pd.read_csv('/Users/anne/Desktop/workspace/data_analysis/movies/movies.dat',sep='::',header=None,names=mnames)

# print(users[:5])
# print(ratings)
# print(movies[:5])
#合并ratings,users,movies
data = pd.merge(pd.merge(ratings,users),movies)
# print(data)

#按性别计算平均分
# mean_ratings = data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
# print(mean_ratings[:5])

#对title进行分组
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])
active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)