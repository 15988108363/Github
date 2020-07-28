def Generating_number():  # 产生随机数字2和4
    import random
    random_number = random.randint(2, 3)
    if random_number == 3:
        random_number += 1
    return random_number


def print_matrix():  # 打印矩阵
    for i in range(4):
        for r in range(4):
            print(game_matrix_list[i][r], end="\t")
        print("\t")
    print("=" * 4)


def Generating_position():  # 数字产生位置,返回插入位置
    import random
    position_number_01 = random.randint(0, 3)
    position_number_02 = random.randint(0, 3)
    while game_matrix_list[position_number_01][position_number_02] != 0:
        position_number_01 = random.randint(0, 3)
        position_number_02 = random.randint(0, 3)
    return position_number_01, position_number_02


def insert_number():  # 插入2或4
    game_matrix_list[position_number_01][position_number_02] = random_number


def Left_methods(list_target):  # 每行左移方法，对目标列表操作将0移动到最右边
    for i in range(len(list_target) - 1, -1, -1):  # 防覆盖从后向前删
        if list_target[i] == 0:
            del list_target[i]
            list_target.append(0)


def Right_methods(list_target):  # 每行右移方法，对目标列表操作将0移动到最左边
    for i in range(len(list_target) - 1, -1, -1):  # 防覆盖从后向前删
        if list_target[i] == 0:
            del list_target[i]
            list_target.insert(0, 0)


def Compare_adjacent_elements(list_target):  # 横向相邻元素比较,并进行加和
    for i in range(len(list_target) - 1, 0, -1):
        if list_target[i] == list_target[i - 1] != 0:
            list_target[i] += list_target[i - 1]
            list_target[i - 1] = 0
            if list_target[i - 2] == list_target[i - 3] != 0:  # 可以再次修改改进
                list_target[i - 2] += list_target[i - 3]
                list_target[i - 3] = 0


def compare_end(list_target):#有问题
    for i in range(4):
        for r in range(3):
            if list_target[i][r] == list_target[i][r + 1]:
                return 1
    for i in range(3):
        for r in range(4):
            if list_target[r][i] == list_target[r][i + 1]:
                return 1
    return 0


def end_game():  # 游戏结束条件
    temp = 1
    if game_matrix_list.count(2048) == 1:
        print("游戏结束\n")
        temp = 0
    elif game_matrix_list.count(0) == 0 and compare_end(game_matrix_list) == 0:
        print("游戏结束\n")
        temp = 0
    return temp


def Matrix_transpose():  # 矩阵转置
    list_transposed_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], ]
    for i in range(4):
        for r in range(4):
            list_transposed_matrix[i][r] = game_matrix_list[r][i]
    game_matrix_list[:] = list_transposed_matrix[:]


def Move_left(list_target):  # 全体左移，做一次加法，0放右面
    list_temp = []
    for r in range(4):
        list_temp = list_target[r]
        Left_methods(list_temp)
        Compare_adjacent_elements(list_temp)
        Left_methods(list_temp)  # 更新矩阵


def Move_right(list_target):  # 全体右移，做一次加法，0放左面
    list_temp = []
    for r in range(4):
        list_temp = list_target[r]
        Right_methods(list_temp)
        Compare_adjacent_elements(list_temp)
        Right_methods(list_temp)  # 更新矩阵


def Move_up(list_target):  # 全体上移，做一次加法，0放下面
    list_temp = []
    Matrix_transpose()
    for r in range(4):
        list_temp = game_matrix_list[r]
        Left_methods(list_temp)
        Compare_adjacent_elements(list_temp)
        Left_methods(list_temp)  # 更新矩阵
    Matrix_transpose()


def Move_down(list_target):  # 全体下移，做一次加法，0放上面
    list_temp = []
    Matrix_transpose()
    for r in range(4):
        list_temp = game_matrix_list[r]
        Right_methods(list_temp)
        Compare_adjacent_elements(list_temp)
        Right_methods(list_temp)  # 更新矩阵
    Matrix_transpose()


def User_instruction():  # 用户指令
    temp = str(input("请输入移动方式(a=左移，d=右移,w=上移，s =下移）：\n"))
    while temp not in ("a", "d", "s", "w"):
        print("输入错误，请重新输入：\n")
        temp = str(input("请输入移动方式(a=左移，d=右移,w=上移，s =下移）：\n"))
    if temp == "w":
        Move_up(game_matrix_list)
    elif temp == "s":
        Move_down(game_matrix_list)
    elif temp == "a":
        Move_left(game_matrix_list)
    elif temp == "d":
        Move_right(game_matrix_list)


# 游戏程序
game_matrix_list = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]  # 初始化矩阵
random_number = Generating_number()  # 随机产生2或4
position_number_01, position_number_02 = Generating_position()  # 数字产生位置,返回插入位置
insert_number()  # 插入2或4
print_matrix()  # 打印矩阵
end_game()  # 初始化结束游戏
while end_game() != 0:
    random_number = Generating_number()  # 随机产生2或4
    position_number_01, position_number_02 = Generating_position()  # 数字产生位置,返回插入位置
    insert_number()  # 插入2或4
    print_matrix()  # 打印矩阵
    User_instruction()  # 用户输入移动方式
    print_matrix()  # 打印矩阵
    end_game()  # 结束游戏判断
