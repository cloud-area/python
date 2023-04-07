# 1.定义类
class Phone:
    # 1.1 方法:开机,关机和拍照
    def open(self):
        print('开机')

    def close(self):
        print('关机')

    def photos(self):
        print('拍照')

# 2.创建对象
phone = Phone()
phone.open()
phone.photos()
phone.close()
