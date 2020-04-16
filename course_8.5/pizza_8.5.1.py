# 结合使用位置实参和任意数量实参
"""如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的
形参放在最后。python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。"""
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
