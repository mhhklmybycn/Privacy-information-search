#本代码写与2022/8/21 雨夜
#作者mhhklmy


#头文件，如果报错请安装4环境pip3 install requests
import requests
import json

#菜单
a = "天云社工工具 by_mhhklmy\n1.qq号查询绑定手机\n2.手机号查询绑定qq\n3.QQ号查询LOL信息\n4.LOL查询QQ信息\n5.QQ号查询老密\n6.微博通过ID查手机号\n7.通过手机号查微博ID\n声明:本项目/工具由mhhklmy编写，接口来自Xapi\n工具仅用于学习与测试，禁止用于违法犯罪。一切后果与作者无关，并拥有最终解释权\n请输入"
x = input(a)

#请求地址
url1 = "https://zy.xywlapi.cc/qqapi?qq="
url2 = "https://zy.xywlapi.cc/qqphone?phone"
url3 = "https://zy.xywlapi.cc/qqlol?qq"
url4 = "https://zy.xywlapi.cc/lolname?name="
url5 = "https://zy.xywlapi.cc/qqlm?qq="
url6 = "https://zy.xywlapi.cc/wbapi?id="
url7 = "https://zy.xywlapi.cc/wbphone?phone="

#主程序
if x == "1":
    qq = input('请输入QQ号：')
    response = requests.get(url1+qq)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('phone'))
    print(json_dict.get('phonediqu'))
elif x == "2":
    phone = input('请输入手机号：')
    response = requests.get(url2+phone)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('qq'))
    print(json_dict.get('phonediqu'))
elif x == "3":
    qq = input('请输入QQ号：')
    response = requests.get(url3+qq)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('name'))
    print(json_dict.get('daqu'))
elif x == "4":
    name = input('请输入游戏名：')
    response = requests.get(url4+name)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('qq'))
    print(json_dict.get('daqu'))
elif x == "5":
    qq = input('请输入QQ号：')
    response = requests.get(url5+qq)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('qq'))
    print(json_dict.get('qqlm'))
elif x == "6":
    id = input('请输入微博ID：')
    response = requests.get(url6+id)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('phone'))
    print(json_dict.get('phonediqu'))
elif x == "7":
    phone = input('请输入手机号：')
    response = requests.get(url7+phone)
    content = response.text
    json_dict = json.loads(content)
    print(json_dict.get('message'))
    print(json_dict.get('id'))
    print(json_dict.get('phonediqu'))
input("输入任意字符结束")
