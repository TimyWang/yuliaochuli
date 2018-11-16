import os
import re
# 从文件中加载数据
fr = open('C:\\Users\\Administrator\\Desktop\\3.txt', 'r', encoding="utf")
fw = open('C:\\Users\\Administrator\\Desktop\\out.txt', mode='w', encoding='utf')
exist_line = []  # 用于过滤比较重复行
r1 = u'mmm'  # 重复部分
for line in fr.readlines():
    line = line.strip()
    line1 = re.search(r1, line)  # 过滤内容
    if line1:
        pass
    else:
        line = line + "\n"
        fw.write(line)  # 写完通过\n进行换行
fw.close()
fr.close()