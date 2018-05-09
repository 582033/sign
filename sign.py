#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
import pdb
from bs4 import BeautifulSoup
from pprint import pprint


class Sign:
    def __init__(self, cookie_path, sign_dict):
        self.cookie_path = cookie_path
        self.sign_dict = sign_dict

    #@site : sign_dict key
    #@info : sign_dict value
    def request(self, site, info):
        #读取cookie
        cookie_file = "%s%s.json" % (self.cookie_path, site)

        #断点调试
        #pdb.set_trace()

        with open(cookie_file) as json_data:
            cookie_list = json.load(json_data)

        #cookie存入dict
        cookie = dict()
        for arr in cookie_list:
            cookie[arr['name']] = arr['value']

        #进行请求
        form_data = info['form'] if 'form' in info else {}
        header_data = info['header'] if 'header' in info else {}

        if (info['method'] == 'get'):
            r = requests.get(info['url'], cookies=cookie, headers=header_data)
        if (info['method'] == 'post'):
            r = requests.post(info['url'], cookies=cookie, data=form_data, headers=header_data)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

    def sign_all(self):
        for site in sign_dict:
            log = self.request(site, sign_dict[site])
            print("[%s] ==  %s" % (site, log))



if __name__ == '__main__':
    cookie_path = '/root/sign/cookie/'
    sign_dict = {
        'jd' : {
            'url'   : 'http://vip.jd.com/index.php?mod=Vip.Ajax&action=signIn&callback=jQuery4415515&_=1469579847791',
            'method' : 'get',
        },
        'tieba' : {
            'url'   : 'http://tieba.baidu.com/sign/add',
            'method' : 'post',
            'form' : {
                    'ie' : 'utf-8',
                    'kw' : '李毅',
                    'tbs' : 'ae7fce58040c07061469429777'
            }
        },
        'smzdm' : {
            'url' : 'http://zhiyou.smzdm.com/user/checkin/jsonp_checkin',
            'method' : 'get',
            'header' : {
                'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:20.0) Gecko/20100101 Firefox/20.0',
                'Host' : 'zhiyou.smzdm.com',
                'Referer' : 'http://www.smzdm.com/'
            }
        }
    }

    sign = Sign(cookie_path, sign_dict)
    sign.sign_all()
