import requests
import os
import json
import time
from Crypto.Cipher import AES
import base64
import re
from urllib.parse import quote
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from time import strftime
from requests.models import Response

global session
# session = requests.session()
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'
}
headers_form = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded'
}
domain_name = 'http://stu.hfut.edu.cn/'
app_id = ''
app_name = ''
name = ''

def Session():
    global session
    session = requests.session()

def get_post_url():
    url = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/casValidate.do?service=/xsfw/sys/swmxsyqxxsjapp/*default/index.do'
    response = session.get(url=url, headers=headers)
    print(response.url)
    return response.url.split('?')[1]

def add_to_16(s):
    while len(s) % 16 != 0:
        s += (16 - len(s) % 16) * chr(16 - len(s) % 16)
    return str.encode(s)  # 返回bytes

def encrypt(text, key):
    aes = AES.new(str.encode(key), AES.MODE_ECB)
    encrypted_text = str(base64.encodebytes(aes.encrypt(add_to_16(text))), encoding='utf8').replace('\n', '')
    return encrypted_text

def check_user_identy(username, password, key):
    password = encrypt(password, key)
    url = 'https://cas.hfut.edu.cn/cas/policy/checkUserIdenty?username=' + username + '&password=' + password + '&_=' + get_stamp().__str__()
    r = session.get(url=url, headers=headers)
    # print(r.headers)
    # print(r.request.headers)
    # print(r.text)
    return password

def get_stamp():
    return int(round(time.time() * 1000))

def jump_auth_with_key():
    """
    获取cookie
    :return:
    """
    jump_auth_url = 'http://stu.hfut.edu.cn/xsfw/sys/emapfunauth/casValidate.do?service=/xsfw/sys/swmxsyqxxsjapp/*default/index.do'
    session.get(url=jump_auth_url, headers=headers)
    JSESSIONID_url = 'https://cas.hfut.edu.cn/cas/vercode'
    session.get(url=JSESSIONID_url, headers=headers)

    LOGIN_FLAVORING_url = 'https://cas.hfut.edu.cn/cas/checkInitVercode?_=' + get_stamp().__str__()
    response = session.get(url=LOGIN_FLAVORING_url, headers=headers)
    return response.cookies.values()[0]

def login(username, password):
    url = 'https://cas.hfut.edu.cn/cas/login?' + get_post_url()
    data = {
        'username': username,
        'captcha': '',
        'execution': 'e1s1',  # 随意
        '_eventId': 'submit',
        'password': password,
        'geolocation': '',
        'submit': '登录'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    }

    response = session.post(url=url, data=data, headers=headers)
    print(response)
    try:
        global app_id
        global app_name
        global name
        html = response.text.replace('\n', '').replace('\r', '').replace(' ', '')
        real_name = re.findall(r'"roleId":"(.+)"}}', html)[0]
        r_list = re.search(r'PATH:path,(.+),RES_SERVER:', html).group(1).replace('"', '').split(',')
        app_id = r_list[0].replace('APPID:', '')
        app_name = r_list[1].replace('APPNAME:', '')
        name=real_name
        print('[+]你好,{}...'.format(real_name))
        return True
    except Exception as e:
        print(e.__str__())
        return False

def get_today_date():
    return time.strftime('%Y-%m-%d', time.localtime())

def pre_post():
    # 为了拿到cookie
    p_url1 = 'http://stu.hfut.edu.cn/xsfw/sys/swpubapp/MobileCommon/getSelRoleConfig.do'  # qw6a
    data = 'data=%7B%22APPID%22%3A%22{}%22%2C%22APPNAME%22%3A%22{}%22%7D'.format(app_id, app_name)
    session.post(url=p_url1, headers=headers_form, data=data)
    p_url2 = 'http://stu.hfut.edu.cn/xsfw/sys/swpubapp/MobileCommon/getMenuInfo.do'  # 5ngm
    session.post(url=p_url2, headers=headers_form, data=data)

def fill_form(username):
    # 开始填写表单
    # pre_post() # 后面都使用5ngm
    # 下面开始填写表单

    def make_data():
        # 提交的数据
        url = 'http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/modules/mrbpa/getStuXx.do'
        data = 'data=%7B%7D'
        response = session.post(url=url, headers=headers_form, data=data)
        r_json = json.loads(response.text)
        post_data = r_json['data']
        return post_data

    post_data = make_data()
    post_data.update({
        "GCKSRQ": "",
        "GCJSRQ": "",
        "DFHTJHBSJ": "",
        "BY1": "1",
        "DZ_SFSB": "1",
        "SZDQ_DISPLAY": "",
        "DZ_SZDQ_DISPLAY": "",
        "JJLXRJG_DISPLAY": ""
    })
    print(post_data)
    data = 'data={}'.format(quote(json.dumps(post_data, ensure_ascii=False).replace(' ', '')))
    post_url = 'http://stu.hfut.edu.cn/xsfw/sys/swmxsyqxxsjapp/modules/mrbpa/saveStuXx.do'
    response = session.post(url=post_url, headers=headers_form, data=data)
    print(response.text)

    # if(username == '2019210356'):
    #     sendMail(username,'1078917027@qq.com',response.text.split('"msg":')[1].replace("}",""))
    # sendMail(username,'1364748092@qq.com',response.text.split('"msg":')[1].replace("}",""))
    # print('\n')

    content=name+"同学\n"+response.text
    # session.get("https://sc.ftqq.com/.send?text=校园打卡+&desp=" + content) server酱推送，可以填入自己的key
    return response

# 自动发送邮件
def sendMail(username,receiver,text):
    mail_host = ''  #设置邮箱服务器
    mail_user = ''  #用户名
    mail_pass = ''  #密码 
    
    sender = ''    
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header("今日校园打卡小助手", 'utf-8')
    message['To'] =  Header("", 'utf-8')
    
    # subject = '今日校园打卡信息'
    message['Subject'] = Header(username+'打卡信息', 'utf-8')
    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 587)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receiver, message.as_string())
        print('邮件发送成功')
    except smtplib.SMTPException:
        print('邮件发送失败')

# username 新版教务用户名
# password 密码
# receive_mail 接收打卡结果的邮箱
def submit(username,password,receive_mail):
    Session()
    key = jump_auth_with_key()
    password = check_user_identy(username, password, key)
    ok = login(username, password)
    if ok:
        pre_post()
        response = fill_form(username)
        sendMail(username,receive_mail,response.text.split('"msg":')[1].replace("}",""))
        return
    else:
        print('登录失败哦...')

def main():
    # 格式化成2016-03-20 11:45:39形式
    print(strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    submit('2020215471','Qqzj121466','1148269334@qq.com') # 设置对应的信息

