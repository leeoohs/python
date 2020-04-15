# 删除包含特定值得所有列表元素

"""方法remove()来删除列中特定的值，之所以可行是因为要删除的值在列表中只出现了一次。
如果要删除列表中所有包含特定值的元素，可不断运行while循环来实现"""

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
