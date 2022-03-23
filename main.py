import time

import requests
import socket
from urllib.parse import parse_qs
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

user_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh-Hans;q=0.9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "http://10.168.6.10",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15",
    "Connection": "keep-alive",
    "Referer": "http://10.168.6.10/",
    "Content-Length": "166"
}
user_data = {
    "DDDDD": ",0,541900000000@cmcc",  # eg：,0,541900000000@cmcc
    "upass": "账号密码",
    "R1": "0",
    "R2": "0",
    "R3": "0",
    "R6": "",
    "para": "00",
    "0MKKey": "123456",
    "buttonClicked": "",
    "redirect_url": "",
    "err_flag": "",
    "username": "",
    "password": "",
    "user": "",
    "cmd": "",
    "Login": ""
}
error_dict = {
    "aW51c2UsIGxvZ2luIGFnYWlu": "多端登录",
    "NTEy": "AC认证失败",
    "dXNlcmlkIGVycm9yMQ==": "账户不存在",
    "QXV0aGVudGljYXRpb24gRmFpbCBFcnJDb2RlPTE2": "非正常时段",
    "dXNlcmlkIGVycm9yMg==": "密码错误"
}


def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def net_status():
    s = socket.socket()
    s.settimeout(1)
    # noinspection PyBroadException
    try:
        status = s.connect_ex(('www.baidu.com', 443))
        if status == 0:
            s.close()
            return True
        else:
            s.close()
            return False
    except Exception:
        return False


def login():
    login_url = 'http://10.168.6.10:801/eportal/?c=ACSetting&a=Login&protocol=http:&hostname=10.168.6.10&iTermType=1&wlanuserip=' + get_ip() + '&wlanacip=10.168.6.9&mac=00-00-00-00-00-00&ip=' + get_ip() + '&enAdvert=0&queryACIP=0&loginMethod=1'
    res = requests.post(login_url, data=user_data, headers=user_headers)
    msg_data = dict(parse_qs(urlsplit(res.url).query))
    soup = BeautifulSoup(res.text, 'lxml')  # 认证成功页
    if soup.title.text == '认证成功页':
        print('连接成功，两秒后退出...')
    else:
        msg = msg_data['ErrorMsg'][0]
        if msg == 'NTEy':
            if net_status():
                print('已连接，两秒后退出...')
            else:
                print('AC认证失败')
        # elif msg == 'aW51c2UsIGxvZ2luIGFnYWlu':
        #     login()
        #     print('抢占登录成功')
        else:
            login()


if __name__ == "__main__":
    login()
    time.sleep(2)
