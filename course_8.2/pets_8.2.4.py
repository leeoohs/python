# 等效的函数调用
def describe_pet(pet_name, animal_type='dog'):
    print(pet_name + " " + animal_type)

# 一条名为willie的小狗
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为harry的仓鼠
describe_pet('harry', 'cat')
describe_pet(pet_name='harry', animal_type='cat')
describe_pet(animal_type='cat', pet_name='harry')
