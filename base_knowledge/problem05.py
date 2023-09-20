# 判断两个JSON数据是否相等
import json


data_01 = {"a":"1", "b":2255, "c":"json_data"}
data_02 = {"a": "1", "b":"2255", "c": "json_data"}
data_03 = {"a":"1", "b":22, "c":"json_data"}


for src_list, dst_list in zip(sorted(data_01), sorted(data_02)):
    if str(data_01[src_list]) != str(data_02[dst_list]):
        print(src_list, data_01[src_list], dst_list, data_02[dst_list])

