import re

# 从文件中加载数据
fr = open('C:\\Users\\Administrator\\Desktop\\out.txt', 'r', encoding="utf")
fw = open('C:\\Users\\Administrator\\Desktop\\out1.txt', mode='w', encoding='utf')
for line in fr.readlines():
    line = line.strip()
    line_no_punctuation = re.sub("[\s+\.\!\/_,$%^*(+\"\')]+|[+——()?【】“”！，。？、~@#￥%……&*（）]+", "", line)
    if 51<=len(line_no_punctuation)<=60:
        line = line + "\n"
        fw.write(line)  # 写完通过\n进行换行
fr.close()
fw.close()