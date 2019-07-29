"""
    2048游戏
    规则：
        游戏运行，在4*4的方格中，出现两个随机数字，
        产生随机数的策略：10% 的概率是4，90%的概率是2
        用户移动方格（wsad），方格内的数字按照相应规则进行合并
        如果地图有变化（数字移动/数字合并），再产生1格随机数
        游戏结束判定：数字不能再合并，也没有空白的位置。
    架构：
        界面视图类（控制台/pygame/...） View
        逻辑处理   Controller
        数据模型模块   Manengr
        程序入口
    步骤：
        1.实现逻辑处理模块
            创建游戏核心类 GameCorController
            （1）将核心算法粘贴进来
            （2）将所有参数改为成员变量
            （3）产生新数字
                    --计算所有空白位置（为0的位置）
                    --随机选择一个位置
                    --根据概率产生数字，存入列表的相应位置
        2.界面视图模块
            创建游戏核心类对象
            调用核心类对象的生成数字
            while Ture:
                呈现界面
                获取用户输入，调用核心类对象的移动方法
                产生随机数
"""
import random
from game2048.model import Location



class GameCorController:
    """
        游戏核心逻辑控制器
    """

    def __init__(self):
        # self.__map = [
        #     [2, 0, 2, 0],
        #     [4, 4, 0, 0],
        #     [2, 4, 0, 2],
        #     [2, 0, 0, 2]
        # ]
        self.__map = [
            [0]*4,
            [0]*4,
            [0]*4,
            [0]*4
        ]
        self.__list_target = []
        # 空位置列表
        self.__list_empty_Location = []
    @property
    def map(self):
        return self.__map

    def zero_to_end(self):
        """
            0往末尾移动
        :return:
        """
        for i in range(len(self.__list_target) - 1, -1, -1):
            if self.__list_target[i] == 0:
                del self.__list_target[i]
                self.__list_target.append(0)

    def merge(self):
        """
            合并两个相邻数字
        :return:
        """
        self.zero_to_end()
        for i in range(len(self.__list_target) - 1):
            # 相邻且相同
            if self.__list_target[i] == self.__list_target[i + 1]:
                self.__list_target[i] += self.__list_target[i + 1]
                self.__list_target[i + 1] = 0
        self.zero_to_end()

    def move_left(self):
        """
            向左移动
        :return:
        """
        m01 = self.map
        for r in range(len(self.__map)):
            self.__list_target[:] = self.__map[r]
            self.merge()
            self.__map[r][:] = self.__list_target
        m02 = self.map
    def move_right(self):
        """
            向右移动
        :return:
        """
        for r in range(len(self.__map)):
            self.__list_target[:] = self.__map[r][::-1]
            self.merge()
            self.__map[r][::-1] = self.__list_target

    def move_up(self):
        for c in range(4):
            self.__list_target.clear()
            for r in range(4):
                self.__list_target.append(self.__map[r][c])
            self.merge()
            for r in range(4):
                self.__map[r][c] = self.__list_target[r]

    def move_down(self):
        for c in range(4):
            self.__list_target.clear()
            for r in range(3, -1, -1):
                self.__list_target.append(self.__map[r][c])
            self.merge()
            for r in range(3, -1, -1):
                self.__map[r][c] = self.__list_target[3 - r]

    def __calculate_empty_Location(self):
        """空位置统计"""
        self.__list_empty_Location.clear()
        for r in range(4):
            for c in range(4):
                if self.__map[r][c] ==0:
                    # 创建空位置
                    loc = Location(r,c)
                    self.__list_empty_Location.append(loc)
    def generate_new_number(self):
        """
            随机生成新数字
        :return:
        """
        self.__calculate_empty_Location()
        if len(self.__list_empty_Location)==0:
            return
        loc =random.choice(self.__list_empty_Location)
        self.__map[loc.r_index][loc.c_index] = 4 if random.randint(1, 10) == 1 else 2
        self.__list_empty_Location.remove(loc)



# def print_map(list_target):
#     """
#         将列表打印到控制台
#     :return:
#     """
#     for r in range(len(list_target)):
#         for c in range(len(list_target[r])):
#             print(list_target[r][c], end=" ")
#         print()


if __name__ =="__main__":
    c01 = GameCorController()
    c01.generate_new_number()
    print_map(c01.map)
    print("-"*20)
    c01.move_left()
    c01.generate_new_number()
    print_map(c01.map)
    print("-"*20)
    c01.move_up()
    c01.generate_new_number()
    print_map(c01.map)
    print("-"*20)
    c01.move_left()
    c01.generate_new_number()
    print_map(c01.map)