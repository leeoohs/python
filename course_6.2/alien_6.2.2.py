# 添加键-值对

"""字典是一种动态结构，可随时在其中添加键-值对。
要添加键-值对，可依次指定字典名、用方括号括起来的键和相关联的值"""

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# 新增键-值对，键为'x_points'，值为0
alien_0['x_points'] = 0
alien_0['y_points'] = 25
print(alien_0)

# 注意，键-值对的排列顺序与添加顺序不同，python不关心键-值对的添加顺序，只关心键和值之间的关联关系
