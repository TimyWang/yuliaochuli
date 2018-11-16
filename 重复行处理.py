# 从文件中加载数据
fr = open('C:\\Users\\Administrator\\Desktop\\3.txt', 'r',encoding="utf-8")
fw = open('C:\\Users\\Administrator\\Desktop\\out.txt', mode='w', encoding='utf-8')
exist_line=[]
for line in fr.readlines():
    line = line.strip()
    if line in exist_line:
        pass
    else:
        exist_line.append(line)
        new_line = line + "\n"
        fw.write(new_line)  # 写完通过\n进行换行
fw.close()
