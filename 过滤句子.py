import os
import re

# 从文件中加载数据
fr = open('C:\\Users\\Administrator\\Desktop\\1.txt', 'r', encoding="utf")
fw = open('C:\\Users\\Administrator\\Desktop\\out3.txt', mode='w', encoding='utf')
exist_line = []  # 用于过滤比较重复行
r2 = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
for line in fr.readlines():
    line = line.strip()
    line2 = re.search(r2, line)  # 过滤内容
    if  line2:
        pass
    else:
        if line in exist_line:
            pass
        else:
            exist_line.append(line)
            new_line = line + "\n"
            fw.write(new_line)  # 写完通过\n进行换行
