# 创建和使用类
# 根据Dog类创建的每个实例都将存储名字和年龄。并赋予小狗蹲下sit()he打滚roll_over()的能力


# 定义一个名为Dog的类，根据约定，python中首字母大写的名称指的是类
# 这个类定义中的括号是空的，因为我们要从空白创建这个类
class Dog():
    """一次模拟小狗的简单尝试"""

    # 方法__init__():类中的函数称为方法，每当根据Dog类创建新实例时，python都会自动运行它
    """我们将方法__init__()定义成了包含三个形参：self、name和age
    在这个方法的定义中，形参self必不可少，还必须未与其他形参的前面。
    为何必须在方法定义中包含形参self呢？因为python调用这个__init__()
    方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法
    调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够
    访问类中的属性和方法。我们创建Dog实例时，python将调用Dog类的方法
    __init__()。我们将通过实参向Dog()传递名字和年龄；self会自动传递，
    因此我们不需要传递它。每当我们根据Dog类创建实例时，都只需给最后两个形参
    （name和age）提供值。"""
    def __init__(self, name, age):
        """初始化属性name和age"""

        """以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何
        实例来访问这些变量。self.name = name获取存储在形参name中的值，并将
        其存储到变量name中，然后该变量被关联到当前创建的实例。像这样可通过实例
        访问的变量称为属性。"""
        self.name = name
        self.age = age

    """Dog类还定义了两个方法：sit()和roll_over()。由于这些方法不需要额外的信息，
    如名字和年龄，因此他们只有一个形参self。"""
    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.tilte() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.tilte() + " rolled over !")
