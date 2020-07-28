from Login import *
user = Login()

#成功返回True
def do_login():
    name = input("User:")
    passwd = input("passwd:")
    return user.login(name,passwd)

def do_register():
    name = input("User:")
    passwd = input("passwd:")
    return user.register(name,passwd)

while True:
    print("=====================")
    print("========login========")
    print("=======register======")
    print("=====================")
    cmd = input("cmd:")
    if cmd == "login":
        if do_login():
            print("登陆成功")
        else:
            print("登录失败")
        break
    elif cmd == "register":
        if do_register():
            print("注册成功")
        else:
            print("注册失败")
        break
    else:
        print("input again")