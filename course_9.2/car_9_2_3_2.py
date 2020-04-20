# 通过方法对属性的值进行递增
"""有时候需要将属性递增特定的量，而不是将其设置为全新的值。
假设我们购买了一辆二手车，且从购买到登记期间增加了100英里的里程，
下面的方法让我们能够传递这个增量，并相应地增加里程表读数"""
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

    def incremert_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles


my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriotive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.incremert_odometer(100)
my_used_car.read_odometer()

