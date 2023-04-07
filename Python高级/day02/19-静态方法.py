# 1.定义类
class Game(object):
    @staticmethod
    def show_menu():
        print('开始')
        print('暂停')
        print('结束')

# 2.调用静态方法
# Game.show_menu()
game = Game()
game.show_menu()