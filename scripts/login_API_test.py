# conding:utf-8
import unittest
from po_api.login_API import Login_API
from libs.ShareModules import GetExcellData
from libs.ShareModules import getFileAbspath


class TestLoginAPI(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass

    def test_01(self):
        print('01')
        # path = getFileAbspath('../data/','账号.xlsx')
        # ed = GetExcellData(path, 0)
        # un_list = ed.getExcelData_Col(1,2)
        # pwd_list = ed.getExcelData_Col(2,2)
        # for i in range(len(un_list)):
        #     r = Login_API(un_list[i],pwd_list[i])
        #     self.assertEqual(r['code'],'1',"状态码变更")
        #     self.assertEqual(r['msg'],"登录成功","提示信息变更")
        #     print('pass-登录成功！',un_list[i])
    def test_02(self):
        print('02')

    def test_03(self):
        print('03')
    # def test_longin_access(self):
    #     r = Login_API('14455551111','123456')
    #     self.assertEqual(r['code'],'1',"状态码变更")
    #     self.assertEqual(r['msg'],"登录成功","提示信息变更")
    #     print('pass-登录成功！')
    # def test_longin_fail_pwd_err (self):
    #     r = Login_API('14455551111','111222')
    #     self.assertEqual(r['msg'],"密码出错啦","提示信息变更")
    #     self.assertEqual(r['code'],2002,"提示码变更")
    #     print('pass-密码错误！')
    # def test_longin_fail_empty(self):
    #     r = Login_API('14512341234','123456')
    #     self.assertEqual(r['msg'],"账号或密码错误,请联系客服","提示信息变更")
    #     self.assertEqual(r['code'],2002,"状态码变更")
    #     print('pass-账号不存在')

if __name__ == '__main__':
    unittest.main(verbosity=3)
    pass