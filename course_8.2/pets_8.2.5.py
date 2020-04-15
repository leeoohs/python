# 避免实参错误：提供的实参多于或少于函数完成其工作所需的信息时，将出现实参不匹配错误
def describe_pet(pet_name, animal_type='cat'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())


describe_pet()

# 执行结果如下：
"""Traceback (most recent call last):
  File "/Users/huangdaxianer./Downloads/subline/project/course_8.2/pets_8.2.5.py", line 8, in <module>
    describe_pet()
"""