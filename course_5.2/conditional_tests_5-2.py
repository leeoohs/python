# 检查两个字符串相等和不相等
car = 'bmw'
print(car == 'bmw')
print(car != 'bmw')

# 使用函数lower()的测试
car = 'Audi'
print(car.lower() == 'audi')
print(car.lower() != 'audi')

# 检查两个数字相等、不等、大于、小于、大于等于和小于等于
number_0 = 3
number_1 = 5
print(number_0 == number_1)
print(number_0 != number_1)
print(number_0 > number_1)
print(number_0 >= number_1)
print(number_0 < number_1)
print(number_0 <= number_1)

# 使用and和or
print(number_0 < 5 and number_1 >5)
print(number_0 < 5 or number_1 > 5)

# 测试特定值是否包含在列表中
cars = ['audi', 'bmw', 'subaru', 'toyota']
print('bmw' in cars)

# 测试特定值是否未包含在列表中
cars = ['audi', 'bmw', 'subaru', 'toyota']
car = 'jeep'

if car not in cars:
    print(car.upper())