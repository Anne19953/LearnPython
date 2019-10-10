#将python数据转换为json格式
import json
data = {
    'name':'myname',
    'age':100
}
json_str = json.dumps(data)
print(json_str)
print(data)

#-------->反序列化，将json格式转为python格式
data = json.loads(json_str)
print(data)

#---------->dumps()用来编码json()格式,并写入文件
with open('test.json','w') as f :
    json.dump(data,f)

#---------->load()读取json文件并将json格式转为python格式读出来
with open('test.json','r') as f:
    data = json.load(f)
    print(data)