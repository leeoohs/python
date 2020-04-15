# 默认值：编写函数时，可给每个形参指定默认值。
# 在调用函数中给形参提供了实参，python将使用制服呢的实参值，否则将使用形参默认值
def describe_pet(pet_name, animal_type='cat'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pet(pet_name='huangshang')

"""使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的形参。
这让python依然能够正确地解读位置实参"""