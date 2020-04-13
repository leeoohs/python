# 确定列表不是空的

# 在制作比萨前检查顾客点的配料列表是否为空
requested_toppings = []

'''在if语句中将列表名用在条件表达式中，python将在列表至少包含一个元素时返回True，
并在列表为空时返回False。如果requested_toppings不为空，就运行与前一个示例相同的for循环'''
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")