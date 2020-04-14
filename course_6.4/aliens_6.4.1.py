# 嵌套
# 字典列表，有时候需要将一系列字典存储在列表中，或将列表作为值存储在字典中，成为嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

# 将字典都放到一个名为aliens的列表中
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)



# 创建一个用于存储外星人的空列表
aliens = []

# 创建30个绿色的外星人
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 10, 'speed': 'medium'}
    aliens.append(new_alien)

# 将前三个外星人修改为黄色的，速度为中等，且值为10
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = '10'
    # 将三个外星人修改为红色，速度为快速，且值为15
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = '15'

# 显示前五个外星人
for alien in aliens[:5]:
    print(alien)
print("...")

# 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))