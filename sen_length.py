from numpy import *
import operator
import os
# 从文件中加载数据
fr = open("C:\\Users\\Administrator\\Desktop\\3.txt", 'r',encoding="utf")
fw = open('C:\\Users\\Administrator\\Desktop\\out.txt', mode='w', encoding='utf')
for line in fr.readlines():
    line = line.strip()
    if len(line)>=10:
        line = line + "\n"
        fw.write(line)  # 写完通过\n进行换行