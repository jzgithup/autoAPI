# coding:utf-8
import requests

def Login_API(username=None, password=None, **kwargs):
    try:
        url = r'https://testuser.zhaoliangji.com/api/login/index'
        data = {}
        if username != None:
            data['username'] = username
        if password != None:
            data['password'] = password
        data.update(kwargs)
        r = requests.post(url, data=data)
        return r.json()
    except:
        print('登录接口错误！')
if __name__ == '__main__':
    r = Login_API('14445551111','1123456')
    print(r)
    pass
