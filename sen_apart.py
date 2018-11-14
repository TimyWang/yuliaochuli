def dateprocess():
    # 从文件中加载数据
    fr = open(r'C:\Users\Administrator\Desktop\output1.txt', 'r', encoding="utf")
    fw1 = open(r'C:\Users\Administrator\Desktop\yunhannum.txt', 'w', encoding="utf")
    fw2 = open(r'C:\Users\Administrator\Desktop\yunhanfirst.txt', 'w', encoding="utf")
    fw3 = open(r'C:\Users\Administrator\Desktop\yunhansecond.txt', 'w', encoding="utf")
    fw4 = open(r'C:\Users\Administrator\Desktop\yunhanlabel.txt', 'w', encoding="utf")
    for line in fr.readlines():
        # 返回移除字符串头尾指定的字符生成的新字符串
        line = line.strip()
        # 以 '\t' 切割字符串
        listFromLine = line.split('\t')
        # 每列的属性数据
        fw1.write(listFromLine[0]+'\n')#字母数字编码
        fw2.write(listFromLine[1]+'\n')#字母数字编码
        fw3.write(listFromLine[2]+'\n')#字母数字编码
        fw4.write(listFromLine[3]+'\n')#字母数字编码

if __name__ == "__main__":
    dateprocess()