# coding=utf-8
# python2
# "http://zhixing.bjtu.edu.cn/uc_server/avatar.php?uid=391524&size=middle"
# http://zhixing.bjtu.edu.cn/space-uid-355382.html
# 2018年8月24日 400382人
import re
import urllib
# 进行URL请求
from bs4 import BeautifulSoup

# 仅仅获取用户名和ID的代码
f = open('name.txt', 'w')
for i in range(1, 400383):

    path2 = 'http://zhixing.bjtu.edu.cn/space-uid-' + str(i) + '.html'
    html2 = str(path2)
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
    # print len(namelist)
    # print namelist[-1]
    # print name[0]  # 打印用户名
    # print namelist[-1]
    print str(i)  # 即为uid编号
    f.write(str(i) + ' , ' + name[0] + '\n')
f.close()