from car import Car,ElectricCar

"""创建一个新车"""
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 里程设置为 23
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()

my_new_car.update_odometer(23)
my_new_car.read_odometer()

"""使用过的车"""
my_used_car = Car('subru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()

"""电动汽车"""
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
