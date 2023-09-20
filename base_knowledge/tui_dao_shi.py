
'''
接口是类或者函数，它可以提供数据服务实现某些功能，也可以作为模块之间传输数据的通道
'''
def f(x, l=[]):
    for i in range(x):
        l.append(i * i)
        print(l)
    print(id(l))
f(2)
f(3, [3, 2, 1])
f(3)