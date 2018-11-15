from numpy import *
import operator
import os
# 从文件中加载数据
fr = open("G:\产品评论语料_10000.txt", 'r',encoding="gbk")
fw = open('产品评论结果.txt', mode='w', encoding='gbk')
for line in fr.readlines():
    line = line.strip()
    if 16<len(line)<=30:
        line = line + "\n"
        fw.write(line)  # 写完通过\n进行换行
