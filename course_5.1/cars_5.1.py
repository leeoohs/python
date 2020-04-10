# 一个简单的示例

# 在一个汽车列表内，将"bmw"汽车名以全大写方式打印，其余以首字母大写方式打印
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    # 检查当前的汽车名是否是'bmw'
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

