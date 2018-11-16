import os
LTP_DATA_DIR = '/home/timwang/PycharmProjects/yuliaochuli/ltp_data'  # ltp模型目录的路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')  # 词性标注模型路径，模型名称为`pos.model`
cws_model_path = os.path.join(LTP_DATA_DIR, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

from pyltp import Postagger,Segmentor

segmentor = Segmentor()
postagger = Postagger()  # 初始化实例
postagger.load(pos_model_path)  # 加载模型
segmentor.load(cws_model_path)

fr = open('/home/timwang/Desktop/yuliao.txt', 'r',encoding="utf")
fw = open('/home/timwang/Desktop/output.txt', mode='w', encoding='utf')
exist_line=[]
for line in fr.readlines():
    line = line.strip()
    if line in exist_line:
        pass
    else:
        exist_line.append(line)
        words = segmentor.segment(line)  # 分词
        postags = postagger.postag(words)   #词性标注
        for postag, word in zip(postags, words):
            fw.write(word + "|" + postag + " ")  # 写完通过\n进行换行
        fw.write("\n")


fw.close()
segmentor.release()  # 释放模型
postagger.release()
