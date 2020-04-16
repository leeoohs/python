# 根据类创建实例
"""可将类视为有关如何创建实例的说明。Dog类是一系列说明，让python
知道如何创建表示特定小狗的实例。"""

class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# my_dog是Dog类的一个实例
"""python使用实参'willie'和6调用Dog类中的方法__init__()。方法__init__()
创建一个表示特定小狗的示例，并使用我们提供的值来设置属性name和age。方法__init__()
并未显式地包含return语句，但python自动返回一个表示这条小狗的实例。
我们将这个实例存在变量my_dog中。在这里，命名约定很有用：
我们通常可以认为首字母大写的名称（如Dog）指的是类，
而小写的名称（如my_dog）指的是根据类创建的实例"""
my_dog = Dog('willie', 6)

# 可按需求根据类创建任意数量数量的实例。
your_dog = Dog('lucy', 3)

# 访问属性：要访问实例的属性，可使用据点表示法
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 调用方法：根据Dog类创建实例后，就可以使用句点表示法来调用Dog类只能给定义的任何方法。
"""要调用方法，可指定实例的名称（这里是my_dog）和要调用的方法，并用句点分隔它们。
遇到代码my_dog.sit()时，python在类Dog中查找方法sit()并运行其代码。"""
my_dog.sit()
my_dog.roll_over()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()
your_dog.roll_over()
