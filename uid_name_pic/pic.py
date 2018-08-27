# coding=utf-8
# python2
# "http://zhixing.bjtu.edu.cn/uc_server/avatar.php?uid=391524&size=middle"
# http://zhixing.bjtu.edu.cn/space-uid-355382.html
# 使用了urllib.urlretrieve
# 2018年8月24日 400382
import re
import urllib

# 进行URL请求
from bs4 import BeautifulSoup

# 这个是头像，命名用的是uid编号+用户名
for i in range(1, 400383):
    path1 = 'http://zhixing.bjtu.edu.cn/uc_server/avatar.php?uid=' + str(i) + '&size=middle'
    path2 = 'http://zhixing.bjtu.edu.cn/space-uid-' + str(i) + '.html'
    html1 = str(path1)  # type: str
    html2 = str(path2)
    # print html1, html2
    page = urllib.urlopen(html2)  # 打开网址
    html3 = page.read()
    bs1 = BeautifulSoup(html3, 'lxml')  # 读取内容并创建beautifulsoup类
    uid = 'space-uid-' + str(i) + '.' + 'html'
    namelist = bs1.find_all(href=re.compile(str(uid)))
    # 这部分总会出现类似[]，即为用户不存在的情况，简单起见，用len（namelist）==0判断
    if len(namelist) == 0:
        continue
    name1 = namelist[-1].encode('utf-8').split('">')  # 以后改下感觉用了诡异的办法，但是结果没问题
    name = name1[-1].split('</a>')
    # print name[0]  # 打印用户名

    urllib.urlretrieve(html1, str(i) + "+" + str(name[0]).decode('utf-8') + '.jpg')
    print str(i)  # 即为uid编号