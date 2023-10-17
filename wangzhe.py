import requests
from lxml import etree
import os
from time import sleep
#伪装
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'}
#获取所有英雄的皮肤
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'   #json文件包含所有英雄的序号，名字等信息 在网络/XHR的标头里
hero_list_resp = requests.get(hero_list_url, headers=headers)

for h in hero_list_resp.json():
    ename = h.get('ename')
    cname = h.get('cname')

    if not os.path.exists(cname):
        os.makedirs(cname)

    #单个英雄主页
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(hero_info_url, headers=headers)
    hero_info_resp.encoding = 'gbk'

    #XPATH方法获得皮肤的名字字段
    e = etree.HTML(hero_info_resp.text)
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    names = [name[0:name.index('&')] for name in names.split('|')]

    #循环得到每个皮肤的图片
    for i, n in enumerate(names):
        # 发送请求
        resp = requests.get(f'https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i + 1}.jpg', headers=headers)
        # 保存
        with open(f'{cname}/{n}.jpg', 'wb') as f:
            f.write(resp.content)