# 给定一个包含正整数且非空的数组，返回该数组中重复次数最多的前N个数字（返回结果按重复次数从多到少降序排列）
def fun01(a: list):
    # 去重
    b = list(set(a))
    # 生成和列表b等长且默认值为0的列表，用于映射生成字典
    list2 = list(0 for x in range(0,len(b)))
    # b与list2映射生成字典代表每一个数字和它出现的次数
    dict01 =dict(zip(b,list2))
    # 遍历目标列表，列表元素每出现一次，字典对应键的值加一
    for i in a:
        dict01[i] += 1
    print(dict01)
    print(dict01.items())
    # 根据value排序
    '''
    lambda x 接收的实参为dict_items([(0, 2), (1, 4), (2, 2), (3, 2), (4, 3), (5, 4), (6, 1), (7, 2), (8, 3), (9, 2)])
    中的每一个元组
    '''
    list03 = sorted(dict01.items(),key=lambda x:x[1],reverse=True)
    print(list03)
list01 = [1, 2, 8, 0, 8, 9, 7, 1, 1, 2, 0, 4, 3, 5, 5, 7, 8, 4, 9, 1, 5, 4, 6, 3, 5]
print(sorted(list01))
fun01(list01)