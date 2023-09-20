''':
对输入的整数数组，输出数组元素中的最大值、最大值的个数、最小值和最小值的个数
函数名称: max_ and_ min(list)
输入参数: list整数数组
输出: list整数数组，有四个值，分别表示最大值、最大值的个数、最小值和最小值的个数
示例: max and. min([1,4,21,5,6,1,1]) => [21,1,1,3]
max_ and. min(1]) => [1,1,1,1]
'''


def max_and_min(source_list):
    source_list.sort()
    max_num = source_list[-1]
    min_num = source_list[0]
    max_count = source_list.count(max_num)
    min_count = source_list.count(min_num)
    print([max_num, max_count, min_num, min_count])

a = [5, 5, 5, 4, 3, 2, 2]
max_and_min(a)
