import sys
import re
#获取命令行参数
port = sys.argv[1]
f=open("1.txt")
#找到port段落
while True:
    date=""
    for line in f:
        if line != "\n":
            date += line
        else:
            break
    if not date:
        print("Not found %s"%port)
        break
    print(date)
    #匹配字符串首个单词
    key_word = re.match(r"\S+",date).group()
    print(key_word)
    if port == key_word:
        try:
            pattern r"[0-9a-f]{4}\.[0-9a-f]{4}\.[0-9a-f]{4}"
            address = re.search(pattren,date).group()
            print(adress)
        except:
            print("Not found %s" % port)
        break

