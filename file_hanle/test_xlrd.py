# xlrd-v1.2读取文件，openpyxl写入文件
import xlrd
import openpyxl
import os
import json



class HandleExcel(object):
    def __init__(self, sheet_name):
        # self.wb = openpyxl.load_workbook(filename=os.path.dirname(__file__)+'/excel_file/login_test_data.xlsx')
        # self.sn = self.wb.get_sheet_names
        self.wb = xlrd.open_workbook(filename=os.path.dirname(__file__) + '/excel_file/login_test_data.xlsx')
        self.sn = self.wb.sheet_by_name(sheet_name)

    def get_data(self):
        data = []
        data_key = self.sn.row_values(0)
        for i in range(1, self.sn.nrows):
            data_value = self.sn.row_values(i)
            unit_case = dict(zip(data_key, data_value))
            # 类型转换
            for k in unit_case.keys():
                try:
                    unit_case[k] = json.loads(unit_case.get(k))
                except (json.decoder.JSONDecodeError, TypeError) as e:
                    continue
            data.append(unit_case)
        # print(json.loads(data[0].get('expect')))
        return data

he = HandleExcel('login')
data = he.get_data()
# headers,data,expect需转换为字典
print(data)