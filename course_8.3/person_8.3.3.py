# 返回字典：函数可返回任何类型的值，包括列表和字典等比较复杂的数据结构
'''def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息,build_person()函数接受名和姓，
    并将这些值封装到字典中，存储first_name的值时，使用的键为first；
    存储last_name的值时使用的键为last"""

    person = {'first': first_name, 'last': last_name}
    return person


musician = build_person('jimi', 'hendrix')
print(musician)'''



# 存储年龄
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('shan', 'huang', age=23)
print(musician)