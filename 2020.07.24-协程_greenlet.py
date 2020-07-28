from greenlet import greenlet
def test1():
    print("执行test1")
    gr02.switch()
    print("结束test1")
    gr02.switch()
def test2():
    print("执行test2")
    gr01.switch()
    print("结束test2")
#将函数变为协程函数
gr01 = greenlet(test1)
gr02 = greenlet(test2)
gr01.switch()#执行协程test1
