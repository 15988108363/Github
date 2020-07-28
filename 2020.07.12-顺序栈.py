"""栈的顺序存储结构
    重点代码
"""
class SStsckError(Exception):
    pass
#基于列表实现顺序栈
class SStack:
    def __init__(self):
        #约定列表最后一个元素为栈顶元素
        self._elems = []
    def top(self):
        if not self._elems:
            raise SStsckError("空栈")
        return self._elems[-1]
    def is_empty(self):
        return  self._elems == []
    def push(self,elems): #入栈
        self._elems.append(elems)
    def pop(self):#出栈
        if not self._elems:
            raise SStsckError("空栈")
        return  self._elems.pop()

if __name__ =="__main__":
    st = SStack()#初始化栈
    # print(st.top())
    print(st.is_empty())
    st.push(12)
    st.push(13)
    st.push(14)
    while not st.is_empty():
        print(st.pop())
str01 = "qeqeqeqwe)eqee(qweqw)wewwe[wqeqwq]wwqwqw{qwqwqw}qs("
st01 = SStack()
for i in str01:
    if i == "(":
        st01.push(1)
    elif i==")":
        st01.push(-1)
num = 0
while not st01.is_empty():
    num += st01.pop()
print(num)
#=======================================
dict01= {"(":")","[":"]","{":"}"}
for i in range(len(str01)):
    if str01[i] in ("(","[","{"):
        st.push(str01[i])
    elif str01[i] in (")","[","}"):
        if st.is_empty() or dict01[st.pop()] != str01[i]:
            print("未匹配错误",str01[i])
            break
if not st.is_empty():
    print("未匹配错误",str01[i])
#===========================================
parens ="()[]{}"
left_parens = "([{"
opposite ={")":"(","]":"[","}":"{"}
def parent(text):
    #i 记录字符串索引
    i,text_len = 0,len(text)
    while True:
        #逐个遍历字符串，如果没遇到结尾并且不是括号就向后遍历
        while i <text_len and text[i] not in parens:
            i +=1
        if i >= text_len:
            return
        else:
            yield text[i],i
            i +=1
st02 = SStack()
for pr,i in parent(str01):
    if pr in left_parens:
        st02.push((pr,i))
    elif st02.is_empty() or st02.pop()[0] != opposite[pr]:#短路运算
        print("unmatching is founded at %d for %s"%(i,pr))
        break
else:
    if st02.is_empty():
        print("all parentheses are matched")
    else:
        print("unmatching is founded at %d for %s"%(st02.pop()))






