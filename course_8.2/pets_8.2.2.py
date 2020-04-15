# 关键字实参：是传递给函数的名称-值对，无需考虑函数调用的实参顺序
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


# 直接在实参中将名称和值关联起来了，因此向函数传递实参时不会混淆
describe_pet(animal_type='cat', pet_name='huangshang')

