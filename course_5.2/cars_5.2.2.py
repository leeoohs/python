# 检查是否相等时不考虑大小写，两个大小写不同的值会被视为不相等

# >>> car = 'Audi'
# >>> car == 'audi'
# False

# 如果大小写无关紧要，只想检查变量的值，可将变量的值转换为小写，再进行比较

# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True
