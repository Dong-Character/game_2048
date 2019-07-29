"""
    显示界面
"""
from game2048.gamecor import *
class GameConsolView:

    def __init__(self):
        self.__target = GameCorController()

    def __print_map(self):
        """
            将列表打印到控制台
        :return:
        """
        for r in range(len(self.__target.map)):
            for c in range(len(self.__target.map[r])):
                print(self.__target.map[r][c], end=" ")
            print()

    def __start_game(self):
        """开始游戏"""
        self.__target.generate_new_number()
        self.__target.generate_new_number()
    def __update(self):
        print("-"*20)
        self.__print_map()
        operate = input("请输入移动方向:")
        if operate =="w":
            self.__target.move_up()
            self.__whether()
        elif operate =="s":
            self.__target.move_down()
            self.__whether()
        elif operate == "a":
            self.__target.move_left()
            self.__whether()
        elif operate == "d":
            self.__target.move_right()
            self.__whether()
        else:
            print("输入错误")
    def __whether(self):
        """判断是否移动"""
        self.__update()
        if self.__print_map() == self.__update():
             self.__target.map[:]= self.__print_map()
        else:
            self.__target.generate_new_number()


    def main(self):
        """
            界面入口方法
        :return:
        """
        self.__start_game()
        while True:
            self.__update()




if __name__ =="__main__":
    GameConsolView().main()