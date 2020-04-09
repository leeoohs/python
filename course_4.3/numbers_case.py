# 使用for循环，打印数字1~20


numbers = []
for value in range(1,21):
    numbers.append(value)
    
print(numbers)


# 使用for循环，打印1~1000000
numbers = []
for value in range(1,1000001):
    numbers.append(value)

print(numbers)

min(numbers)
max(numbers)
sum(numbers)

# 打印1~20的奇数

numbers = []
for value in range(1,21,2):
    numbers.append(value)

print(numbers)


# 打印3~30内能被3整除的数

numbers = []
for value in range(3,31,3):
    numbers.append(value)

print(numbers)


# 列表解析
numbers = [value for value in range(3,31,3)]
print(numbers)


# 打印1~10的立方


numbers = []
for value in range(1,11):
    numbers.append(value**3)

print(numbers)

# 列表解析
numbers = [value**3 for value in range(1,11)]
print(numbers)