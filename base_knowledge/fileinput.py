import random
# 随机生成10个数并写入文件
f = open('./file.txt','a')
list1 = []
for i in range(10):
    num = random.randint(0,10)
    list1.append(str(num))
f.write(','.join(list1))
f.close()
