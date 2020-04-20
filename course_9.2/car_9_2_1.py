# 使用类和实例
"""你可以使用类来模拟现实世界中的很多场景。类编写好后，你的大部分时间都将花在使用
根据类创建的实例上。你需要执行额一个重要任务是修改实例的属性。你可以直接修改实例的
属性，也可以编写方法以特定的方式进行修改。"""

# 下面编写一个表示汽车的类，它存储了有关汽车的信息，还有一个汇总这些信息的方法
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())