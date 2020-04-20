# 修改属性的值
"""可以以三种不同的方式修改属性的值：直接通过实例进行修改；
通过方法进行设置；通过方法进行递增（增加特定的值）"""

# 直接修改属性值：通过实例直接访问它
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


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriotive_name())
# 我们使用句点表示法来直接访问并设置汽车的属性odometer_reading
# 这行代码让python在实例my_new_car中找到属性odometer_reading，并将该属性的值设置为23
my_new_car.odometer_reading = 23
my_new_car.read_odometer()


