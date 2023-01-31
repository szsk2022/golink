"""
Name : QQbot
version : 1.3
Goto_version : 2.7
Time : 2022/12/26
E-mail : zhy@sunzishaokao.com
Name : 张浩阳

"""
from flask import Flask, request
import base64
import requests
import time
import random
import hashlib
import json
import pickle
import threading
import traceback
class bot_mian:
    def __init__(s):
        s.label=s.r_str()
        s.data=[]
        s.Z_admin=[123,234]
        s.kfz=False
        s.lq={# 口令:(冷却分钟,id)
            '提交链接':(5,0),
            '冷却测试':(61,1)
            }
        s.kl=[('菜单',s.CaiDan,0),
              ('仓库地址',s.CangKuDiZhi,0),
              ('提交链接',s.LianJie_add,1),
              ('链接状态',s.LianJieZhuangTai,1),
              ('调试模式',s.TiaoShiMoShi,0),
              ('联系我们',s.LianXiWoMen,0),
              ('公众号留言',s.GongZhongHaoLiuYan,0),
              ('加入QQ群',s.JiaRuQQun,0),
              ('微信客服',s.WXKeFu,0),
              ('提交工单',s.TiJiaoGongDan,0),
              ('取消链接',s.LianJie_del,1),
              ('通过审核链接',s.LianJie_TongGuo,1),
              ('添加管理员',s.Admin_add,1),
              ('取消管理员',s.Admin_del,1),
              ('查看待审核链接',s.LianJie_see,0),
              ('查看管理员列表',s.Admin_see,0),
              ('查看所有链接',s.Lianjie_see_all,0),
              ('查询口令冷却时间',s.LengQue_see,0),
              ('AdminHome',s.GuanLiCaiDan,0)
            #   ('传入测试数据',s.Test_Data,1)
              ]
        s.ts=[
            #   ('调试模式',s.TiaoShiMoShi,0),
               ('执行代码',s.exec_,1),
               ('冷却测试',s.pd_user,0),
               ('关闭服务',s.Close_fw_1,0),
               ('永久关闭服务',s.Close_fw_2,0)
             ]
        s.url='https://go.sunzishaokao.com/'
        s.gocq_api='http://127.0.0.1:5700'
        s.accessKey='AK'
        s.secretKey='SK'
        s.gocq_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36"}
        s.get_token()
        # 每隔5分钟检查一次是否有新的待审核链接
        threading.Thread(target=s.get_url_list_cx).start()
        # 检查冷却信息是否有效
        s.jc_lq()
        # 0启动，1暂时关闭，2永久关闭
        s.js=0
    def main(s,m):
        message = m['message'].strip()
        if s.js==0:
            if not(s.kfz and s.pd_user(m) == 'admin'):
                for i in s.kl:
                    if i[2]:# 头
                        if message[:len(i[0])] == i[0]:
                            if s.pd_lq(i[0],m):
                                i[1](m)
                            else:
                                t=s.lq_time(i[0],m)
                                s.send(m,f'此口令处于冷却期，{t}后可以正常使用')
                    else:# 整
                        if message == i[0]:
                            if s.pd_lq(i[0],m):
                                i[1](m)
                            else:
                                t=s.lq_time(i[0],m)
                                s.send(m,f'此口令处于冷却期，{t}后可以正常使用')
            else:
                for i in s.ts+s.kl:
                    if i[2]:# 头
                        if message[:len(i[0])] == i[0]:
                            try:
                                if s.pd_lq(i[0],m):
                                    i[1](m)
                                else:
                                    t=s.lq_time(i[0],m)
                                    s.send(m,f'此口令处于冷却期，{t}后可以正常使用')
                            except:
                                s.send(m,'错误：\n'+traceback.format_exc())
                                print(traceback.format_exc())
                    else:# 整
                        if message == i[0]:
                            try:
                                if s.pd_lq(i[0],m):
                                    i[1](m)
                                else:
                                    t=s.lq_time(i[0],m)
                                    s.send(m,f'此口令处于冷却期，{t}后可以正常使用')
                            except:
                                s.send(m,'错误：\n'+traceback.format_exc())
                                print(traceback.format_exc())
        elif s.pd_user(m) == 'admin' and message == '启动服务' and s.js==1:
            s.js=0
            s.send(m,'服务已启动！')
    def lq_time(s,kl,m):
        users=s.get_lq_users()
        id=s.lq[kl][1]
        data=users[m['user_id']]
        s_t=s.get_timestamp()-data[id]
        s_t=s.lq[kl][0]*60-s_t
        if s_t>=3600:
            t=f'{s_t//3600}时{(s_t%3600)//60}分{s_t%60}秒'
        elif s_t>=60:
            t=f'{s_t//60}分{s_t%60}秒'
        elif s_t:
            t=f'{s_t}秒'
        return t
    def r_str(s,mun=10):
        a=list('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890')
        b=''
        for i in range(8):
            b+=a[random.randint(0,len(a)-1)]
        return b
    def get_lq_users(s):
        with open ('./lq.txt')as f:
            lq_users=f.read().split('\n')
        a={}
        for i in lq_users:
            try:
                i=i.split(':')
                j=i[1].split(',')
                i=i[0]
                j=[int(b) for b in j]
                a[int(i)]=j
            except:
                pass
        return a
    def save_lq_users(s,users):
        text=''
        for i in users:
            text+=str(i)+':'
            for j in users[i]:
                text+=str(j)+','
            text=text[:-1]
            text+='\n'
        with open('lq.txt','w')as f:
            f.write(text)
    def pd_lq(s,kl,m,Save=True):
        if kl in s.lq:# 口令是否在冷却列表内
            users=s.get_lq_users()# 获取用户列表
            if m['user_id'] not in [i for i in users]:# 用户是否在冷却txt内
                users[m['user_id']]=[0]*len([i for i in s.lq])# 如果没有，则生成一个
                s.save_lq_users(users)     # 保存
            id=s.lq[kl][1]
            data=users[m['user_id']]# 提出用户
            if s.get_timestamp()-data[id] >=s.lq[kl][0]*60:#
                users[m['user_id']][id]=s.get_timestamp()
                if Save:
                    s.save_lq_users(users)
                return True
            else:
                return False
        return True
    def get_url_list_cx(s):
        while 1:
            a=s.post_API('api/get/data',s.get_headers(),{'condition':'status','value':0})
            print(a)
            data=a['data']
            t=[]
            if data:
                for i in data:# 提醒列表
                    if i not in s.data:
                        s.data.append(i)
                        t.append(i)
            for i in s.data:# 旧列表
                if i not in data:
                    s.data.remove(i)
            if t:
                text='有新的链接待审核：'
                for i in t:
                    text+=f'\nID:{i["ID"]}  url:{i["url"]}'
                s.send({'message_type':'group','group_id':123456},text,at=0)
            else:
                print('无待审核')
            time.sleep(60*5)
    def jc_lq(s):
        users=s.get_lq_users()
        l=len([i for i in s.lq])
        for i in users:
            if len(users[i]) !=l:
                users[i]=[0]*l
        s.save_lq_users(users)
    def Close_fw_1(s,m):
        s.js=1
        s.send(m,'服务已关闭！发送 启动服务 即可继续服务！')
    def Close_fw_2(s,m):
        s.js=2
        s.send(m,'服务已关闭！重启进程可启动服务！')
    def send(s,m,text,at=True):
        if m['message_type'] == 'group':
            if at:
                text='[CQ:at,qq='+str(m['user_id'])+']\n'+text
            urls = s.gocq_api+"/send_group_msg?group_id=" + str(m['group_id']) + "&message=" + text
            requests.post(url=urls,headers=s.gocq_headers)
        elif m['message_type']=='private':
            urls = s.gocq_api+"/send_msg?user_id=" + str(m['user_id']) + "&message=" + text
            requests.post(url=urls,headers=s.gocq_headers)
    def post_API(s,api,headers,data):
        return requests.post(s.url+api,headers=headers,data=json.dumps(data)).json()
    def get_timestamp(s):
        return int(time.time())
    def get_token(s):
        t=s.get_timestamp()
        headers={"Content-Type":"application/json",'label':s.label}
        sign_=s.accessKey+s.secretKey+str(t)+'BYROY'
        sign=hashlib.sha512(sign_.encode("utf-8")).hexdigest()
        data={'timestamp':str(t),
              'accessKey':s.accessKey,
              'sign':sign}
        data=s.post_API('api/get/auth',headers,data)
        if data['status'] != 200:
            s.token='Error'
        else:
            s.token=base64.b64decode(data['token'])
    def get_headers(s):
        a=s.post_API('api/detection/auth',{"Content-Type":"application/json",'label':s.label},{})
        if not a['key']:
            s.get_token()
        return {"Content-Type":"application/json",'label':s.label,'token':s.token}
    def pd_user(s,m):
        try:
            with open("admins.pickle",'rb') as f:
                admin_s = pickle.load(f)
        except:
            with open("admins.pickle",'wb') as f:
                pickle.dump([],f)
            admin_s=[]
        if m['user_id'] in admin_s or m['user_id'] in s.Z_admin:
            return 'admin'
        else:
            return 'user'

    def exec_(s,m):
        def print(text):
            s.send(m,str(text),at=0)
        exec(m['message'][4:])





    #-----------通用口令-----------#
    # 查询口令冷却时间
    def LengQue_see(s,m):
        users=s.get_lq_users()
        text='口令冷却信息：'
        for i in s.lq:
            text+='\n'+i+'：'
            if s.pd_lq(i,m,False):
                text+='未冷却'
            else:
                text+=f'剩余{s.lq_time(i,m)}'
        s.send(m,text)
    # 菜单
    def CaiDan(s,m):
        s.send(m,'''————主菜单————
仓库地址 提交链接
链接状态 联系我们
查询口令冷却时间
————GoTo————''')
    # 仓库地址
    def CangKuDiZhi(s,m):
        s.send(m,'''Gitee: https://gitee.com/szsk/golink
官方网站：https://go.sunzishaokao.com''')
    # 链接状态
    def LianJieZhuangTai(s,m):
        url=m['message'][4:].replace(' ','')
        a=s.post_API('api/get/data/status',s.get_headers(),{'url':url})
        if s.kfz and s.pd_user(m) == 'admin':
            s.send(m,'返回：'+str(a))
        try:
            if a['code'] == 0:
                s.send(m,'''您的链接为待审核
GoTo团队将会在72小时内审核您的链接，请保持网站正常！''')
            elif a['code'] == 1:
                s.send(m,'''您好，您的链接状态为: 正常''')
            elif a['code'] == 2:
                s.send(m,'''您好，您的链接状态为：不合法''')
            elif a['code'] == 3:
                s.send(m,'''您好，您的链接状态为：封禁''')
        except:
            s.send(m,'错误：'+a['error'])
    # 联系我们
    def LianXiWoMen(s,m):
        s.send(m,'''1.	公众号留言
2.	加入QQ群
3.	微信客服
4.	提交工单''')
    # 公众号留言
    def GongZhongHaoLiuYan(s,m):
        s.send(m,'''请您微信搜一搜“孙子烧烤知识分享站”,或者手机微信扫描二维码关注我们
[CQ:image,file=https://static.limenoon.com/image/20221213075600.png]''')
    # 加入QQ群
    def JiaRuQQun(s,m):
        s.send(m,'''您好，我们的官方QQ群号为：609642152，欢迎您的加入!''')
    # 微信客服
    def WXKeFu(s,m):
        s.send(m,'''请使用手机微信点击
https://work.weixin.qq.com/kfid/kfcccbc5c65c7b2a468获取人工服务！''')
    # 提交工单
    def TiJiaoGongDan(s,m):
        s.send(m,'请访问https://www.sunzishaokao.com/提交工单 处提交您的问题！')

    # 提交链接
    def LianJie_add(s,m):
        url=m['message'][4:].replace(' ','')
        a=s.post_API('api/submit/robot',s.get_headers(),{'mode':s.pd_user(m),'url':url})
        if s.kfz and s.pd_user(m) == 'admin':
            s.send(m,'返回：'+str(a))
        if s.pd_user(m) == 'admin':
            if a['status'] != 200:
                s.send(m,f'添加链接 {url} 失败：{a["error"]}。如有问题请联系支持客服')
            else:
                s.send(m,f'您好，已添加链接 {url} ！')
        else:
            if a['status'] != 200:
                s.send(m,f'添加链接 {url} 失败：{a["error"]}。如有问题请联系支持客服')
            else:
                s.send(m,f'您好，您提交的链接为 {url} 已进入审核期，请耐心等待审核')
    #-----------管理口令----------#
    # 系统信息
    def SYS_info(s,m):
        if s.pd_user(m) == 'admin':
            data=s.post_API('/system/info?action=cpu&type=json',s.get_headers(),{'action':'cpu','type':'json'})

    # 查看待审核链接列表
    def LianJie_see(s,m):
        if s.pd_user(m) == 'admin':
            a=s.post_API('api/get/data',s.get_headers(),{'condition':'status','value':'0'})
            data=a['data']
            if data:
                text='待审核列表：'
                for i in data:
                    text+='\nUrl：'+i['url']
                s.send(m,text)
            else:
                s.send(m,'现在没有待审核链接！')
        else:
            s.send(m,'您非管理员用户，无权查询待审核链接！')
    # 取消链接
    def LianJie_del(s,m):
        if s.pd_user(m) == 'admin':
            url = m['message'][4:].replace(' ', '')
            a = s.post_API('api/change/data', s.get_headers(), {'mode': 'cancel', 'url': url})
            if a['status'] != 200:
                s.send(m,f'取消链接{url}失败！{a["errer"]}')
            else:
                s.send(m,f'已取消链接{url}！')
        else:
            s.send(m,'您非管理员用户，无权取消链接！')
    # 通过审核链接
    def LianJie_TongGuo(s,m):
        if s.pd_user(m) == 'admin':
            url = m['message'][6:].replace(' ', '')
            a = s.post_API('api/change/data', s.get_headers(), {'mode': 'pass', 'url': url})
            if a['succ'] == 0:
                s.send(m,f'通过审核链接{url}失败：{a["error"]}')
            else:
                s.send(m,f'已通过审核链接{url}！')
        else:
            s.send(m,'您非管理员用户，无权通过审核链接！')
    # 调试模式
    def TiaoShiMoShi(s,m):
        if s.pd_user(m) == 'admin':
            if s.kfz:
                s.kfz = False
                s.send(m,'已关闭调试模式！')
            else:
                s.kfz = True
                s.send(m,'已开启调试模式！')
        else:
            s.send(m,'您非管理员用户，无权打开调试模式')
    # 管理菜单
    def GuanLiCaiDan(s,m):
        if s.pd_user(m) == 'admin':
            s.send(m,'''-----管理菜单-----
调试模式
添加管理员 QQ号码
取消管理员 QQ号码
取消链接 网址
通过审核链接 网址
查看管理员列表
查看待审核链接
查看所有链接
-----GoTo-------''')
        else:
            s.send(m,'''您非管理员用户，无权查看该菜单！''')


    # 添加管理员
    def Admin_add(s,m):
        if m['user_id'] in s.Z_admin:
            admin = m['message'][5:].replace(' ', '')
            try:
                int(admin)
            except:
                s.send(m,'格式错误！')
            else:
                try:
                    try:
                        with open("admins.pickle", 'rb') as f:
                            admins = pickle.load(f)
                    except:
                        with open("admins.pickle", 'wb') as f:
                            pickle.dump([int(admin)], f)
                    else:
                        with open("admins.pickle", 'wb') as f:
                            pickle.dump(admins+[int(admin)], f)
                except:
                    s.send(m,'添加管理员失败！')
                else:
                    s.send(m,f'已添加{admin}为管理员')
        else:
            s.send(m,'您非超级管理员用户，无权添加管理员！')
    # 取消管理员
    def Admin_del(s,m):
        if m['user_id'] in s.Z_admin:
            admin = m['message'][5:].replace(' ', '')
            try:
                int(admin)
            except:
                s.send(m,'格式错误！')
            else:
                try:
                    with open("admins.pickle", 'rb') as f:
                        admins = pickle.load(f)
                    # print(admins)
                    with open("admins.pickle", 'wb') as f:
                        admins.remove(admin)
                        pickle.dump(admins, f)
                except:
                    s.send(m,f'已取消{admin}的管理员')
                else:
                    s.send(m,f'已取消{admin}的管理员')
        else:
            s.send(m,'您非超级管理员用户，无权取消管理员！')
    # 查看管理员
    def Admin_see(s,m):
        if s.pd_user(m) == 'admin':
            with open("admins.pickle", 'rb') as f:
                admins = pickle.load(f)
            text='管理员列表: '
            for i in admins:
                text+=str(i)+','
            text=text[:-1]
            s.send(m,text)
        else:
            s.send(m,'您非管理员用户，无权查看管理员列表！')
    # 查看所有链接
    def Lianjie_see_all(s,m):
        if s.pd_user(m) == 'admin':
            datas={}
            # 获取状态并储存
            for i in range(4):
                data_=s.post_API('api/get/data',s.get_headers(),{'condition':'status','value':str(i)})['data']
                print(data_)
                if data_:
                    for data in data_:
                        datas[int(data['ID'])]={'url':data['url'],'ID':data['ID'],'type':['待审核','正常','不合法','封禁'][i]}
            # 排序
            data=[]
            for i in sorted(datas):
                # print(datas)
                data.append(datas[i])
            if data:
                text='链接列表：'
                for i in data:
                    text+=f"\nID:{i['ID']}  Url:{i['url']}  状态:{i['type']}"
                s.send(m,text)
            else:
                s.send(m,'链接里空空如也~')
        else:
            s.send(m,'您非管理员用户，无权查询所有链接！')
    # 提交测试数据
    def Test_Data(s,m):
        message=m['message'][6:].replace(' ', '')
        message=message.split(',')
        test={'user_id':int(message[0]),'message':message[1],'message_type':m['message_type']}
        if m['message_type'] == 'group':
            test['group_id']=m['group_id']
        s.main(test)
        s.send(m,'已提交！')
bot=bot_mian()
app = Flask(__name__)
@app.route("/", methods=['POST'])
def mian():
    m = json.loads(request.stream.read().decode('utf8'))
    threading.Thread(target=bot.main, args=(m,)).start()
    return ''
app.run(port=5702, debug=True)
