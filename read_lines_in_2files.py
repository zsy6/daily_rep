file1 = open('0907.txt','r',encoding='utf-8')    
file2 = open('0906.txt','r',encoding='utf-8')    
#这个文本文档采用的是gbk编码，这个时候我们需要转换成python能识别的编码，比如utf-8
while 1:
    line1 = file1.readline()
    line2 = file2.readline()
    print(line1)
    print(line2)
    if not (line1 or line2):
        break