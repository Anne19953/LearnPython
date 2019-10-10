#1.实现了不需要改变原函数的情况下进行认证（china(),ameria()等函数内部代码结构未改变）
#2.调用方法不变，依然是american(),china()
#3.用户可以选择不同的认证方法
user_status = False #用户登录后状态改为True
def login(auth_type):#把要执行的模块从这里传进来
    def auth(func):
        def inner(*args,**kwargs):#再定义一层函数
            if auth_type == 'qq':
                _username = 'songfengju'
                _password = 'abc123'
                global user_status
                if user_status == False:
                    username = input('user:')
                    password = input('passeord:')

                    if username == _username and password == _password:
                        print('welcome login...')
                        user_status = True
                    else:
                        print('wrong username or password!')

                if user_status == True:
                    return func(*args,**kwargs) #只要验证通过，就调用相应功能

            else:
                print('only aupport qq')
        return inner  #用户调用login时，
            # 只会返回inner的内存地址，下次再调用时加上()才会执行inner函数
    return auth





def home():
    print('--------首页--------')
@login('qq')
def america():
    print('------欧美专区------')
@login('weibo')
def japan():
    print('-----日本专区-------')
@login('qq')
def china(style):
    print('--------大陆专区------')


home()
america()
japan()
china('shazi')












