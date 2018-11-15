import os
import re
from pyltp import Segmentor

LTP_DATA_DIR = 'D:\ltp_data'  # ltp模型目录的路径
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`
segmentor = Segmentor()  # 初始化实例
segmentor.load(cws_model_path)  # 加载模型
# 从文件中加载数据
fr = open('D:\corpus\人机对话语料_分句_去重.txt', 'r', encoding="utf")
fw = open('D:\corpus\人机对话语料_分句_去重_分词结果2.txt', mode='w', encoding='utf')
exist_line = []  # 用于过滤比较重复行
r1 = u'[a-zA-Z’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】[\\]^_`{|}~]+'  # 正则表达式
r2 = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
for line in fr.readlines():
    line = line.strip()
    line1 = re.search(r1, line)  # 过滤内容
    line2 = re.search(r2, line)  # 过滤内容
    if line1 or line2:
        pass
    else:
        if line in exist_line:
            pass
        else:
            exist_line.append(line)
            words = segmentor.segment(line)  # 分词
            new_line = '\t'.join(words) + "\n"
            fw.write(new_line)  # 写完通过\n进行换行
fw.close()
segmentor.release()  # 释放模型