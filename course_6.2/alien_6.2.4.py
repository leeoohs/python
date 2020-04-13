# 修改字典中的值

# 修改字典中的值，可依次指定字典名、用方括号括起的键以及与该键相关联的新值。
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")


# 例子
alien_0 = {'x_position': 0, 'y_posiotion': 25, 'speed': 'medium'}
print("Original x_position is " + str(alien_0['x_position']) + ".")

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外形恩的速度一定很快
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x_position: " + str(alien_0['x_position']) + ".")

# 将中等速度的外星人变成速度很快的外星文
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外形恩的速度一定很快
    x_increment = 3

# 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New new x_position: " + str(alien_0['x_position']) + ".")
