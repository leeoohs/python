# 继承
"""编写类时，并非总是要从空白开始。如果你要编写的类是另一个现成类的特殊版本，
可使用继承。一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；原有的类
称为父类，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的
属性和方法。"""

# 子类的方法__init__()
"""创建子类的实例时，python首先需要完成的任务是给父类的所有属性赋值。为此，子类
的方法__init__()需要父类施以援手。"""
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


"""c创建子类时，父类必须包含在当期文件中，且位于子类前面。
我们定义了子类ElectricCar。定义子类时，必须在括号内指定父类的名称。
方法__init__()接受创建Car实例所需的信息。"""
class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类的属性，super()是一个特殊的函数，帮助python将父类和子类联系起来。
        这行代码让python调用ElectricCar的父类的方法__init__()，让ElecticCar实例包含
        父类的所有属性。父类也称为超类，名称super因此而得名。"""
        super().__init__(make, model, year)


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())