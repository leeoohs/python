# 复制列表

# 要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）
my_foods = ['pizza', 'falafel', 'carrot cake']
# 我们在不指定任何索引的情况下从列表my_foods中提取一个切片，从而创建了这个列表的副本，再将该副本存储到变量friend_foods中。
friend_foods = my_foods[:]

# 为核实我们确实有两个列表，在每个列表内都分别添加一个不同的食品：
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are")
print(friend_foods)