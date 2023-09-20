# 列表中除a[i]外所有元素的积，不使用除法。（前缀积和后缀积应用）
def solution(l: list):
    n = len(l)
    premul = [1]
    sufmul = [1]
    result = []
    # premul[i]为前i个元素的积
    for i in range(1, n + 1):
        m = premul[i - 1] * l[i - 1]
        premul.append(m)
    print(premul)

    # sufmul[i]为后i个元素的积
    i = n
    while i > 0:
        m = sufmul[n - i] * l[i - 1]
        sufmul.append(m)
        i -= 1
    print(sufmul)

    for i in range(n):
        m = premul[i] * sufmul[n - i - 1]
        result.append(m)
    for i in range(n):
        print('except the test_list[%d]' % (i), end=' ')
        print(result[i])

test_list = [1, 2, 3, 4, 5, 6]
# [24,12,8,6]
solution(test_list)
