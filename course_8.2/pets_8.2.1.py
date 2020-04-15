# 传递实参:位置实参，关键字实参
"""位置实参：你调用函数时，python必须将函数调用中的每个实参都关联到函数定义中的一个形参。
为此，最简单的关联方式是给予实参的顺序，这种关联方式被称为位置实参。"""
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


# 位置实参的顺序很重要，与形参的顺序一一对应
describe_pet('cat', 'huangshang')
# 调用函数多次，可以根据需要调用函数任意次。要再描述一个宠物，只需再次调用describe_prt()
describe_pet('hamster', 'harry')
