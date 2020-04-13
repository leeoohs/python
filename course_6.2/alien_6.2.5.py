# 删除键-值对，可使用del语句将相应的键-值对彻底删除
# 使用del语句时，必须指定字典名和要删除的键
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)

# 注意：删除的键-值对永远消失了
