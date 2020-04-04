from enum import Enum

class case_lines(Enum):
    case_code = 1   #用例编码
    case_model = 2  #功能模块
    case_link = 3   #接口地址
    case_re_method = 4  #请求方式
    case_check = 5  #测试项
    case_excute = 6 #是否执行

