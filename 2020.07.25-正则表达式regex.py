import re
s = "Levi:1994,Sunny:1993"
pattern = r"(\w+):(\d+)"
#re模块调用
l01 = re.findall(pattern,s)
print(l01)

#compile对象调用
regex = re.compile(pattern)
pos =0
endpos=12
l02 = regex.findall(s,0,12)
print(l02)
l03 = re.split(r"[^\w]+","how are  you l-qwww-1';asds as")
print(l03)
s = "时间：2020/7/25"
ns = re.subn(r"/","-",s)
print(ns)
s = "2019年建国70周年"
pattern = r"\d+"
iter01= re.finditer(pattern,s)
print(iter01)
for i in iter01:
    print(i,i.group())
#完全匹配
m= re.fullmatch(r"\w+","hello-1973")
print(m)
#匹配开始位置
m= re.match(r"[A-Z]\w+","Hello 1973")
print(m.group())
#匹配开始位置第一处
m= re.search(r"\S+","Hello 1973")
print(m.group())
print("=================================================")
pattern=r"(ab)cd(?P<pig>ef)"
regex = re.compile(pattern)
#获取match对象
match_obj=regex.search("abcdefghijklmnopasdfghjjxcv",pos=0,endpos=17)
#属性变量
print(match_obj.pos)
print(match_obj.endpos)
print(match_obj.re)
print(match_obj.string)
print(match_obj.lastgroup)
print(match_obj.lastindex)
print(match_obj.span())
print(match_obj.start())
print(match_obj.end())
print(match_obj.groupdict())
print(match_obj.groups())
print(match_obj.group("pig"))