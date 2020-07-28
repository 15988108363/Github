import re
s = """Hello World,
你好，北京！"""
regex = re.compile(r"\w+")
l01 = regex.findall(s)
print(l01)

#只能匹配ACCII码字符
regex= re.compile(r"w+",flags=re.A)
l = regex.findall(s)
print(l)
#忽略字母大小写
regex = re.compile(r"[a-z]+",flags=re.I)
l = regex.findall(s)
print(l)
regex = re.compile(r".+",flags=re.X)
l = regex.findall(s)
print(l)
regex = re.compile(r"^你",flags= re.M)
l = regex.findall(s)
print(l)
regex = re.compile(r"d,$",flags= re.M)
l = regex.findall(s)
print(l)
pattern = r"""\w+ #第一部分
\s+ #第二部分
\w+ #第三部分
"""
regex = re.compile(pattern,flags= re.X|re.M)
l = regex.findall(s)
print(l)