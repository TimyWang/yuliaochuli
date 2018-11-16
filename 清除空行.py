# coding = utf-8
def clearBlankLine():
    file1 = open('C:\\Users\\Administrator\\Desktop\\corpus.txt', 'r', encoding='utf') # 要去掉空行的文件
    file2 = open('C:\\Users\Administrator\\Desktop\\out.txt', 'w', encoding='utf') # 生成没有空行的文件
    try:
        for line in file1.readlines():
            if line == '\n':
                line = line.strip("\n")
            file2.write(line)
    finally:
        file1.close()
        file2.close()


if __name__ == '__main__':
    clearBlankLine()
