#coding:utf-8
import requests
import redis
from bs4 import BeautifulSoup
from time import sleep
from pprint import pprint
def gethot():
    head = {
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
    }

    apps = {}
    content = []
    for i in range(1,40):
        r = requests.get('http://app.mi.com/topList?page=' + str(i), headers = head)
        soup = BeautifulSoup(r.text)
        with open('hotdata', 'w') as f:
            f.writelines(soup.get_text("\n", strip=True))
        with open('hotdata', 'r') as f:
            html = f.readlines()

        content += html[12:108]
        sleep(0.5)

        
    content = content[::-1]
    record = 0
    #把游戏单独拿出来
    gametypes = ['模拟经营',  '动作枪战', '格斗快打', '体育运动', '跑酷闯关', '网游RPG', '战争策略', '赛车体育',  '棋牌桌游', '塔防迷宫', '儿童益智', '飞行空战', 'VR']
    apps["游戏"] = []
        
    for i in range(len(content)):
        if i % 2 == 0:
            record = content[i].rstrip('\n')
            if record not in apps.keys() and record not in gametypes:
                apps[record] = []
        elif i % 2 == 1:
            if record in gametypes:
                apps["游戏"].append(content[i].rstrip('\n'))
            else:
                apps[record].append(content[i].rstrip('\n'))

    #pprint(apps)
    #pprint(apps.keys())
    conn = redis.StrictRedis(host='127.0.0.1',decode_responses=True, port=6379, db=0)
    conn.hmset("hotapps", apps)
    #utfapps = conn.hgetall("hotapps")
    #pprint(utfapps)

if __name__ == '__main__':
    gethot()
