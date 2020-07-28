from threading import Thread,Event
from time import sleep
s = None#全局变量用于通信
e =Event()
def Yangzirong():
    print("杨子荣前来拜山头：")
    global s
    s = "天王盖地虎"
    e.set()#结束阻塞

t = Thread(target=Yangzirong)
t.start()
print("说对口令进入山寨")
e.wait()#阻塞等待
if  s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他")
t.join()