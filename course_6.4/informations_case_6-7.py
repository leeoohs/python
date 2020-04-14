# 创建三个表示人的字典
informations_0 = {
    'first_name': 'kai',
    'last_name': 'liu',
    'age': 22,
    'city': 'beijing',
    }

informations_1 = {
    'first_name': 'shan',
    'last_naame': 'huang',
    'age': 28,
    'city': 'beijing',
    }

informations_2 = {
    'first_name': 'shang',
    'last_name': 'huang',
    'age': 5,
    'city': 'tianjin'
    }

peoples = [informations_0, informations_1, informations_2]

for people in peoples:
    print(people)