'''
用python写一个函数,将一个字符串中给定的子串字符按从小到大的输出，第一个字符的位置为0
如: myOrder( abejykhsesm’,2,5),起始位置，截取长度
输出:ehjky
'''

def myOrder(source_str, start, len):
    target_str = source_str[start:len + start]
    s1 = list(target_str)
    s1.sort()
    s2 = ''.join(s1)
    print(s2)
    # print(sorted(target_str))

myOrder('abejykhsesm', 2, 5)