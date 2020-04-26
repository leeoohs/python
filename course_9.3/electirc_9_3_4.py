# 重写父类的方法
"""对于父类的方法，只要它不符合子类模拟的实物的行为，都可对其进行重写。
为此，可在子类中定义一个这样的方法，即它与要重写的父类方法同名。
这样，python将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。"""

# 假设Car类有一个名为fill_gas_tank()的方法，它对全电动车车来说还无意义，因此需要重写
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
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-KWh battery.")

    def fill_gas_tank(self):
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
