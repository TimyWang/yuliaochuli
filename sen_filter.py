from numpy import *
import re

# 从文件中加载数据
fr = open('D:\corpus\la.txt', 'r', encoding="gbk")
fw = open('D:\corpus\out.txt', mode='w', encoding='gbk')
for line in fr.readlines():
    line = line.strip()
    line = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", line)
    if 20 < len(line):
        line = line + "\n"
        fw.write(line)  # 写完通过\n进行换行
fr.close()
fw.close()