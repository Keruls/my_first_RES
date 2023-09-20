def fibo(num):
    a = 0
    b = 1
    counter = 0
    while counter<num:
        yield a
        a,b=b,a+b
        counter +=1

res = fibo(5)
print(next(res))
print(next(res))
print(next(res))
print(next(res))
print(next(res))