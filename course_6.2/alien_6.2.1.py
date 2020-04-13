# 使用字典，字典是一系列间-值对，每个键都是一个值相关联，可以使用键来访问与之相关的值

# 访问字典中的值，要获取与键相关联的值，可依次指定字典名和放在方括号内的键
alien_0 = {'color': 'green'}
print(alien_0['color'])

# 字典中可包含热议数量的键-值对
alien_0 = {'color': 'green', 'points': 5}

# 现在可以访问外星人的颜色和点数。从字典中获取与'points'相关联的值并存储到new_points中
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
