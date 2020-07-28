class Vector2:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_vector02(self):
        print("该向量是（%d,%d）" % (self.x, self.y))

    def get_elements(list_target, v_pos, v_dir, count):
        result = []
        for i in range(count):
            v_pos.x += v_dir.x
            v_pos.y += v_dir.y
            result.append(list_target[v_pos.x][v_pos.y])
        return result

    @classmethod
    def up(self, list_target, v_pos, count):
        result = []
        for i in range(count):
            v_pos.x += -1
            v_pos.y += 0
            result.append(list_target[v_pos.x][v_pos.y])
        return result

    @classmethod
    def down(self, list_target, v_pos, count):
        result = []
        for i in range(count):
            v_pos.x += 1
            v_pos.y += 0
            result.append(list_target[v_pos.x][v_pos.y])
        return result

    @classmethod
    def right(self, list_target, v_pos, count):
        result = []
        for i in range(count):
            v_pos.x += 0
            v_pos.y += 1
            result.append(list_target[v_pos.x][v_pos.y])
        return result

    @classmethod
    def left(self, list_target, v_pos, count):
        result = []
        for i in range(count):
            v_pos.x += 0
            v_pos.y += -1
            result.append(list_target[v_pos.x][v_pos.y])
        return result


