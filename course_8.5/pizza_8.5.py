# 传递任意数量的实参，python允许函数从调用语句中收集任意数量的实参
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

"""形参名*toppings中的星号让python创建一个名为toppings的空元祖，
并将收到的所有值都封装到这个元组中。函数体内的print语句通过生成输出来证明
python能够处理使用一个调用函数的情形，也能处理使用三个值来调用函数的情形"""

# 现在将这条print语句替换为一个循环，对配料列表进行遍历
def make_pizza(*toppings):
    """概述要制作的比萨"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')