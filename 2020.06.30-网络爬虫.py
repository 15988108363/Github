import urllib.request
# noinspection PyUnresolvedReferences
import chardet

# 对应网页的网网址
url = "http://www.51garlic.com/suanp/show-htm-itemid-9797.html"
page = urllib.request.urlopen(url)
# 读取网页
htmlCode = page.read()
# 转换格式
date = htmlCode.decode("utf-8")

pagefile = open("d:\\我的文档\\桌面\\tempFile.txt", "wb")
pagefile.write(htmlCode)  # 写入文件
pagefile.close()

# 目标文字的前部分
firstString = "<div>"
# 目标文字的后部分
followString = '</div>'

aimStringFirstIndex = 0
aimStringEndIndex = 0
beginIndex = 0


def getAimCode(line, firstString, beginIndex):
    return line.find(firstString, beginIndex)


file = open('d:\\我的文档\\桌面\\tempFile.txt', 'r', encoding='UTF-8')

fileOut = open("d:\\我的文档\\桌面\\大蒜价格.txt", "w", encoding="UTF-8")

for line in file:
    beginIndex = 0
    beginIndex = getAimCode(line, firstString, beginIndex)
    if beginIndex != -1:
        # -1表示要超早的字符串不存在
        # 下标位置移动到目标的汉字的起始位置
        beginIndex += firstString.__len__()
        aimStringFirstIndex = beginIndex
        # 从要截取文字的起始位置开始查找，提高效率
        aimStringEndIndex = getAimCode(line, followString, beginIndex)
        if aimStringEndIndex == -1:
            continue

    fileOut.write(line[aimStringFirstIndex:aimStringEndIndex] + "\n")
    pass
file.close()