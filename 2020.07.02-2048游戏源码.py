#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 作者：魏明泽
# 参考网址: http://2048game.com/
import random
import math

__mataclass__ = type  # 使用新式类

# 此类为地图模块封装的类
class map2048():

    # 重新设置游戏数据
    def reset(self):
        self.__row = 4  # 行数
        self.__col = 4  # 列数
        self.data = [
            [0 for x in range(self.__col)]
            for y in range(self.__row)
        ]
        # self.data = [[x + 4 * y for x in range(self.__col)]
        #              for y in range(self.__row)]
        # self.data = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
        self.fill2()
        self.fill2()

    def __init__(self):
        self.reset()

    # 获取没有数字的位置的个数
    def get_space_count(self):
        """
        获取没有数字的方格的数量
        """
        count = 0
        for r in self.data:
            count += r.count(0)
        return count

    # 获取游戏的得数。
    def get_score(self):
        s = 0
        for r in self.data:
            for c in r:
                s += 0 if c < 4 else c * int((math.log(c, 2) - 1.0))
        return s

    # 填充2到空位置，如果填度成功返回True,如果已满，则返回False,
    def fill2(self):
        blank_count = self.get_space_count()
        if 0 == blank_count:
            return False
        # 生成随机位置
        pos = random.randrange(0, blank_count)
        offset = 0
        for r in self.data:
            for ci in range(self.__col):
                if 0 == r[ci]:
                    if offset == pos:
                        r[ci] = 2
                        return True
                    offset += 1

    # 判断游戏是否结束
    def is_gameover(self):
        for r in self.data:
            # 如果水平方向还有0,则游戏没有结束
            if r.count(0):
                return False
            # 水平方向如果有两个相邻的元素相同，则没有游戏结束
            for i in range(self.__col - 1):
                if r[i] == r[i + 1]:
                    return False
        for c in range(self.__col - 1):
            # 竖直方向如果有两个相邻的元素相同，则没有游戏结束
            for r in range(self.__row - 1):
                if self.data[r][c] == self.data[r + 1][c]:
                    return False
        # 以上都没有，则游戏结束
        return True

    # 2048游戏的左移动 (采用"贾琳倩"美女老师的方法进行移动)
    def left(self):
        # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值
        moveflag = False
        # 将所有数字向左移动来填补左侧空格
        for times in range(self.__col - 1):
            for r in self.data:
                for c in range(self.__col - 1):
                    if 0 == r[c]:
                        moveflag = True
                        r[c] = r[c + 1]
                        r[c + 1] = 0
        # 判断是否发生碰幢，如果有碰撞则合并,合并结果靠左，右则填充空格
        for r in self.data:
            for c in range(self.__col - 1):
                if r[c] == r[c + 1]:
                    moveflag = True
                    r[c] *= 2
                    r[c + 1] = 0
        # 再将所有数字向左移动来填补左侧空格
        for times in range(self.__col - 1):
            for r in self.data:
                for c in range(self.__col - 1):
                    if 0 == r[c]:
                        moveflag = True
                        r[c] = r[c + 1]
                        r[c + 1] = 0
        return moveflag

    # 游戏右移操作
    def right(self):
        for r in self.data:
            r.reverse()
        moveflag = self.left()
        for r in self.data:
            r.reverse()
        return moveflag

    # 游戏上移操作
    def up(self):
        # moveflag 是否成功移动数字标志位,如果有移动则为真值,原地图不变则为假值
        moveflag = False
        # 将所有数字向上移动来填补上面空格
        for times in range(self.__row - 1):
            for c in range(self.__col):
                for r in range(self.__row - 1):
                    if 0 == self.data[r][c]:
                        moveflag = True
                        self.data[r][c] = self.data[r + 1][c]
                        self.data[r + 1][c] = 0
        # 判断是否发生碰幢，如果有碰撞则合并,合并结果靠上，下面填充空格
        for c in range(self.__col):
            for r in range(self.__row - 1):
                if self.data[r][c] == self.data[r + 1][c]:
                    moveflag = True
                    self.data[r][c] *= 2
                    self.data[r + 1][c] = 0
        # 再将所有数字向上移动来填补上面空格
        for times in range(self.__row - 1):
            for c in range(self.__col):
                for r in range(self.__row - 1):
                    if 0 == self.data[r][c]:
                        moveflag = True
                        self.data[r][c] = self.data[r + 1][c]
                        self.data[r + 1][c] = 0
        return moveflag

    # 游戏下移操作
    def down(self):
        self.data.reverse()
        moveflag = self.up()
        self.data.reverse()
        return moveflag


import sys

if (sys.version_info > (3, 0)):
    from tkinter import *
    from tkinter import messagebox
else:
    from Tkinter import *

game = map2048()

keymap = {
    'a': game.left,
    'd': game.right,
    'w': game.up,
    's': game.down,
    'Left': game.left,
    'Right': game.right,
    'Up': game.up,
    'Down': game.down,
    'q': exit,
}

game_bg_color = "#bbada0"
mapcolor = {
    0: ("#cdc1b4", "#776e65"),
    2: ("#eee4da", "#776e65"),
    4: ("#ede0c8", "#f9f6f2"),
    8: ("#f2b179", "#f9f6f2"),
    16: ("#f59563", "#f9f6f2"),
    32: ("#f67c5f", "#f9f6f2"),
    64: ("#f65e3b", "#f9f6f2"),
    128: ("#edcf72", "#f9f6f2"),
    256: ("#edcc61", "#f9f6f2"),
    512: ("#e4c02a", "#f9f6f2"),
    1024: ("#e2ba13", "#f9f6f2"),
    2048: ("#ecc400", "#f9f6f2"),
    4096: ("#ae84a8", "#f9f6f2"),
    8192: ("#b06ca8", "#f9f6f2"),
}

# 游戏各方块的lable数据
map_labels = []


# 鼠标按下处理函数
def on_mouse_down(event):
    print("clicked at", event.x, event.y)


# 键盘按下处理函数
def on_key_down(event):
    keysym = event.keysym
    if keysym in keymap:
        if keymap[keysym]():
            game.fill2()
    update_ui()
    if game.is_gameover():
        mb = messagebox.askyesno(title="gameover", message="游戏结束!\n是否退出游戏!")
        if mb:
            exit()
        else:
            game.reset()
            update_ui()


# 刷新界面函数
def update_ui():
    # 更改各个Label的设置
    for r in range(len(game.data)):
        for c in range(len(game.data[0])):
            number = game.data[r][c]
            label = map_labels[r][c]
            label['text'] = str(number) if number else ''
            label['bg'] = mapcolor[number][0]
            label['foreground'] = mapcolor[number][1]
    label_score['text'] = str(game.get_score())


# 以下为2048的界面
root = Tk()
root.title('2048')
# root.iconbitmap('./favicon.ico')  # 48x48 ico bitmap

frame = Frame(root, width=300, height=300, bg=game_bg_color)
frame.grid(sticky=N + E + W + S)
# 按键事件见：http://blog.csdn.net/qq_25600055/article/details/46942035
# 设置焦点能接收按键事件
frame.focus_set()
frame.bind("<Key>", on_key_down)
# 以下绑定鼠标按下事件
# frame.bind("<Button-1>", on_mouse_down)
# 以下绑定鼠标移动事件
# frame.bind("<Motion>", on_mouse_down)
# 以下绑定鼠标抬起事件
frame.bind("<ButtonRelease-1>", on_mouse_down)
# 见 :http://blog.csdn.net/wjciayf/article/details/50550947


# 初始化图形界面
for r in range(len(game.data)):
    row = []
    for c in range(len(game.data[0])):
        value = game.data[r][c]
        text = '' if 0 == value else str(value)
        label = Label(frame, text=text, width=4, height=2,
                      font=("黑体", 30, "bold"))
        label.grid(row=r, column=c, padx=5, pady=5, sticky=N + E + W + S)
        row.append(label)
    map_labels.append(row)
bottom_row = len(game.data)
print("button", str(bottom_row))
label = Label(frame, text='分数', font=("黑体", 30, "bold"),
              bg="#bbada0", fg="#eee4da")
label.grid(row=bottom_row, column=0, padx=5, pady=5)
label_score = Label(frame, text='0', font=("黑体", 30, "bold"),
                    bg="#bbada0", fg="#ffffff")
label_score.grid(row=bottom_row, columnspan=2, column=1, padx=5, pady=5)


def reset_game():
    game.reset()
    update_ui()


# restart_button = Button(frame, text='重新开始', command=reset_game)
restart_button = Button(frame, text='重新开始', font=("黑体", 16, "bold"),
                        # width=4, height=2,
                        bg="#8f7a66", fg="#f9f6f2", command=reset_game)
restart_button.grid(row=bottom_row, column=3, padx=5, pady=5)

update_ui()

root.mainloop()