# 给予定义属性和方法
"""让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。"""

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        """添加了薪属性self.battery_size，并设置其初始值（如70）。根据ElectricCar
        类创建的所有实例都将包含这个属性，但所有Car实例都不包含它。"""
        self.battery_size = 70

    """添加一个名为describe_battery()的方法，它打印有关电瓶的信息。"""
    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()