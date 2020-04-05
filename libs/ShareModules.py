# coding:utf-8
import xlrd
import os
import copy

import unittest
# -------------------------------------------------------------------------------
# 函数的目的：获取Excel中数据
class GetExcellData():
    def __init__(self,filepath,sheetID,wb=None,sheet=None):
        self.filepath = filepath
        self.sheetID = sheetID
        self.wb = wb
        self.wb = xlrd.open_workbook(filepath)
        self.sheet = sheet
        self.sheet = self.wb.sheet_by_index(sheetID)
    # -------------------------------------------------------------------------------
    # 函数的目的：获取表格内容行数和列数
    def getExcelDataRowCount(self):
        '''获取指定单元格内容'''
        try:
            row_count = self.sheet.nrows
            return row_count
        except:
            print("获取表格行数失败")
    # -------------------------------------------------------------------------------
    # 函数的目的：获取表格内容列数
    def getExcelDataColCount(self):
        '''获取指定单元格内容'''
        try:
            col_count = self.sheet.ncols
            return col_count
        except:
            print("获取表格列数失败")
    # -------------------------------------------------------------------------------
    # 函数的目的：获取指定单元格内容
    # row：行号    clo：列号
    def getExcelData_P(self, row, clo):
        '''获取指定单元格内容'''
        try:
            key = self.sheet.col_values(row - 1, clo - 1, clo)
            return key[0]
        except:
            print('获取excel文件指定表格对应单元格数据失败')
    # -------------------------------------------------------------------------------
    # 函数的目的：获取一行内容，从第N列开始
    # row：行号    start_col：列号
    def getExcelData_Row(self, row, start_col=1):
        '''获取一行内容，从第N列开始'''
        try:
            key = self.sheet.row_values(row-1, start_col-1)
            return key
        except:
            print('读取excel表中某一行数据失败')

    # -------------------------------------------------------------------------------
    # 函数的目的：获取一列内容，从第N行开始
    # row：行号    start_col：列号
    def getExcelData_Col(self, col, start_row=1):
        '''获取一列内容，从第N行开始'''
        try:
            key = self.sheet.col_values(col-1,start_row-1)
            return key
        except:
            print('读取excel表中某一行数据失败')

# 获取文件绝对路径
# local_dir:本地文件路径   filename：文件名
def getFileAbspath(local_dir):
    try:
        abspath = os.path.abspath(local_dir)
        return abspath
    except:
        print('获取文件绝对路径失败')
# 将请求参数写入字典
# data：字符串形式获取表格数据
def setRequestDataForDic(data:str):
    try:
        dic = {}
        datalist = data.split(',')
        for i in datalist:
            s = i.split('=')
            dic[s[0]] = s[1]
        return dic
    except:
        print('请求参数写入失败')
# 过滤测试集、测试用例
# path：用例地址 colID：判断条件列id   colstr：判断条件字符串
# 返回参数：list[编号]
def getExcelTestSuiteOrTestCases(path,sheetID,colID,colstr):
    try:
        t = []
        data = GetExcellData(path, sheetID=sheetID)
        row_count = data.getExcelDataRowCount()
        for i in range(row_count):
            tests = data.getExcelData_Row(i+1,1)
            if tests[colID] == colstr:
                # 将不执行的测试集/测试用例添加到列表中
                t.append(tests[0])
    except:
        pass
    return t

# 获取要执行的测试集
def getTestSuite(discover):
    try:
        cover_suite = copy.deepcopy(discover)
        # 过滤不需要执行的模块
        casepath = getFileAbspath('../testcases/testcase1.xlsx')
        m = getExcelTestSuiteOrTestCases(casepath,1,1,'NO')
        for i in range(len(m)):
            for j in range(discover._tests.__len__()):
                d = discover._tests[j]
                if m[i] in str(d):
                    cover_suite._tests.remove(d)
        return cover_suite
    except:
        print('获取执行的测试模块失败')
# 获取要执行的测试用例
def getTestCases(discover_suite):
    try:
        cover_cases = copy.deepcopy(discover_suite)
        # 过滤不需要执行的用例
        casepath = getFileAbspath('../testcases/testcase1.xlsx')
        t = getExcelTestSuiteOrTestCases(casepath,0,6,'NO')
        for i in range(len(t)):
            for j in range(discover_suite._tests.__len__()):
                s_m = discover_suite._tests[j]
                for k in range(s_m._tests.__len__()):
                    s_c = s_m._tests[k]
                    for l in range(s_c._tests.__len__()):
                        s_t = s_c._tests[l]
                        if t[i] == s_t._testMethodName:
                            cover_cases._tests[j]._tests[k]._tests.remove(s_t)
        return cover_cases
    except:
        print('获取执行的测试用例失败')

if __name__ == '__main__':
    discover = unittest.defaultTestLoader.discover('../scripts', pattern='*_test.py')
    casepath = getFileAbspath('../testcases/testcase1.xlsx')
    print(casepath)
    d = getExcelTestSuiteOrTestCases(casepath,1,1,'NO')
    print(d)
    # m = getTestSuite(discover)
    # c = getTestCases(m)
    # print(c)

    # d = setRequestDataForDic('asd=1,bvc=2')
    # print(d)
    # path1 = os.path.abspath(r'../data')
    # path2 = os.path.join(path1, '账号.xlsx')
    # print(path2)
    # path2 = getFileAbspath('../data','账号.xlsx')
    # r = GetExcellData(path2,0)
    # print(r.getExcelDataCount())
    # print(r.getExcelData_P(1,2))
    # print(r.getExcelData_Row(1))
    # print(r.getExcelData_Col(1,2))


    pass

