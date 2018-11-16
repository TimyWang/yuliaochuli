#-*- coding:utf-8 -*-
from pyltp import Segmentor
from pyltp import Postagger
from pyltp import Parser
import os
LTP_DIR = 'D:\\ltp_data/'
print(os.path.join(LTP_DIR,'cws.model'))
segmentor = Segmentor()  # 初始化实例
segmentor.load(os.path.join(LTP_DIR,'cws.model'))  # 加载模型
postagger =  Postagger()
postagger.load(os.path.join(LTP_DIR,'pos.model'))
parser =  Parser()
parser.load(os.path.join(LTP_DIR,'parser.model'))

def segment(sent):
    words = segmentor.segment(sent)
    words_list = list(words)
    for word in words_list:
        print (word)
    # segmentor.release()  # 释放模型
    return words_list

def postag(word_list):
    postags = postagger.postag(word_list)
    for postag in postags:
        print (postag)
    # segmentor.release()  # 释放模型
    return postags

def dep_parser(word_list,pos_list):
    arcs = parser.parse(word_list,pos_list)
    print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))

word_list = segment('释放模型')
pos_list = postag(word_list)
arcs = dep_parser(word_list,pos_list)