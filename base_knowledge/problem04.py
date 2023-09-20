'''
字符串右补齐，根据len长度补齐str到src中
函数名称： rpad(src,len,str)
输入参数:：src原字符串, len目标字符串长度, str用来填充的字符串
输出：补齐后的字符串

示例：
rpad (“abcd”,10,“12”) =>“abcd121212”
rpad (“abcd”,11,“12”) =>“abcd1212121”
rpad (“abcd”,10,“12”) =>"abcd121212”
rpad (“abd”,12,“0”) =>"bd0000000”
rpad (“abcd”,12," ") =>"abcd
'''


def rpad(src, tar_len, g_str):
    # 差几个字符
    n_str = tar_len - len(src)
    if n_str<=0: print(src)
    else:
        # 取余数，整除数
        tar_str = src + g_str * (n_str // len(g_str)) + g_str[:n_str % len(g_str)]
        print(tar_str)


rpad("abcd", 10, "121212121212")   # 10位
rpad("bbbb", 11, "12")   # 11位
rpad("cccc", 12, "12")  # 12位
rpad("dddd", 13, "0")  # 13位
rpad("ffff", 13, " ")  # 13位有空格
