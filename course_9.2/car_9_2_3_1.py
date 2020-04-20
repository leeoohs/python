# 通过方法修改属性的值
"""如果有替你更新属性的方法，将大有裨益。这样，你就无需直接访问属性，
而可将值传递给一个方法，由它在内部进行更新"""

class Car():
    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriotive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    """对Car类所做的唯一修改是添加了方法update_odometer()，这个方法接受一个里程值，
    并将其存储到self.odometer_reading中。"""
    def update_odometer(self, mileage):
        """将里程表读数设定为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriotive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()