import os

LTP_DATA_DIR = 'D:\ltp_data'  # ltp模型目录的路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`

from pyltp import Postagger

postagger = Postagger()  # 初始化实例
postagger.load(pos_model_path)  # 加载模型

fr = open('D:\corpus\la分词结果.txt', 'r', encoding="gbk")
fw = open('D:\corpus\conll词性标注结果.txt', mode='w', encoding='gbk')
for line in fr.readlines():
    line = line.strip()
    words = line.split('\t')
    postags = postagger.postag(words)  # 词性标注""
    for index, pos in enumerate(postags):
        fw.write(str(index) + "\t" + words[index] + "\t" + words[index] + "\t" + pos + "\t" + pos + "\t" + "\t" + "_" +"\t" + "_" +"\t" + "_" + "\t" + "_" +"\t" + "_" + "\n")  # 写完通过\n进行换行
    fw.write("\n")
fw.close()
postagger.release()  # 释放模型