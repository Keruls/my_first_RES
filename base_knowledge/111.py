from decimal import Decimal
import datetime




class Person():
    n = 2
    def __init__(self,age:int,name:str):
        self.age = age
        self.name = name
        self.lan_list = []
    @staticmethod
    def eat():
        print(Person.n)

    def speak(self):
        sl = ''
        p = ','
        for i,j in enumerate(self.lan_list):
            if i==(len(self.lan_list)-1):
                p = ''
            sl += ('%s%s'%(j, p))
        s = 'i am {}, {} years old, i can speak {}.'.format(self.name, self.age, sl)
        print(s)
    def learn(self,*language:str):
        for i in language:
            self.lan_list.append(i)

class Student(Person):
    m = 3
    def __init__(self,age ,name, leave):
        super().__init__(age,name)
        self.leave = leave
        print(super())

    def my_leave(self):
        print('now my leave is:',self.leave)

    @staticmethod
    def gett():
        print('555555555555555')

Student.gett()

# l = tuple((1,1,5,7,1,2,3,3,5,5,4,4,6))
# st = {1,2,3,6,5,4}
# s = set(l)
# print(l)
# for i in st:
#     print(i,end='')
# print(list(s))
#
# thisset = {'1','2','8','0'}
# print(thisset)


# # 装饰器
# def decoration(old_fn):
#     # *args, **kwargs accept any params.
#     def make_new(*args, **kwargs):
#         print('decorated begin!')
#         # *args, **kwargs are analysed.
#         old_fn(*args, **kwargs)
#         print('decorated end!')
#     return make_new
#
# def fn1(a):
#     print('i am fn1,my param is:', a)
#
# # 装饰方法1
# fn3 = decoration(fn1)
# fn3(456)
#
# # 装饰方法2,fn2被装饰了
# @decoration
# def fn2(a: int, b: str):
#     print('i am fn1,my param is:%d and %s' % (a, b))
#
# fn2(1111, 'ppppp')


# 闭包
# def bbox():
#     p = []
#     def average(n):
#         p.append(n)
#         return sum(p) / len(p)
#     return average
# s = bbox()
# print(s(10))
# print(s(20))

# def fun():
#     a=10
#     a +=1
#     print(a)
# fun()
# fun()
# def fun(n):
#     if (n == 1):
#         return 1
#     return n*fun(n - 1)
# print(fun(10))

# i = 10
# while (i > 0):
#     k = 1
#     for j in range(1, i + 1):
#         k *= j
#     i -= 1
#     print(k)

# k = 1
# for j in range(1, 11):
#     k *= j
# print(k)


# a = [1, 2]
# b = {'n': 1, 'm': 2}
# c = 10
#
# def fun3():
#     a.append(99999)
#     print(a)
# fun3()
# print(a)


# a = 9
# b = 7.0
# # c = float(Decimal(str(a)) + Decimal(str(b)))
# d = 1
# e = '1'
# f = 1.0
# s1 = 'aaaaaa'
# s2 = 'bbbbbb'
# i = 0

# while i<5:
#     for j in list(range(5)):
#         print('*', end='')
#         print('j=', j, end='')
#     print('')
#     i += 1

# x = ['a', 'a', 3, 3]
#
#
# def fun1(x, **y):
#     print(x)
#     print(y)
#     return
# fun1(x=1,i='sdaf',y=456,d=[1,2,'yuyuieeee'])e

# str1 = '123{}456789'.format(datetime.datetime.now())
# print(str1)
# str1 = 'hellow%s'%(s1)
# print(str1)
# str2 = 'hellow%3.5s'%('123456789')
# print(str2)
# str3 = '%shellow%s'%('123456789','123456789')
# print(str3)

# if d == f:
#     print('equal')
# else:
#     print('not equal')

# if c == 0.3:
#     print(c)
#     print(type(c))
# else:
#     print(c)
#     print(type(c))
#     print('error')
