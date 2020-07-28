import module02
if __name__ =="__main__":#如果程序从当前模块运行，则执行下列的测试代码
#如果当前模块被主模块导入，则下列测试代码不再执行
    list01 = [
        ["00", "01", "02", "03"],
        ["10", "11", "12", "13"],
        ["21", "22", "23", "24"],
        ["31", "32", "33", "34"],
        ["41", "42", "43", "44"]
    ]

s01 = module02.Vector2(2, 3)
s02 = module02.Vector2(4, 3)
s03 = module02.Vector2(2, 6)
s04 = module02.Vector2(8, 3)

s01.print_vector02()
s02.print_vector02()
s03.print_vector02()
s04.print_vector02()

result = module02.Vector2.get_elements(list01, module02.Vector2(2, 1), module02.Vector2(0, 1), 2)
print(result)

result = module02.Vector2.up(list01, module02.Vector2(2, 1), 2)
print(result)

result = module02.Vector2.down(list01, module02.Vector2(2, 1), 2)
print(result)

result = module02.Vector2.left(list01, module02.Vector2(2, 1), 2)
print(result)

result = module02.Vector2.right(list01, module02.Vector2(2, 1), 2)
print(result)