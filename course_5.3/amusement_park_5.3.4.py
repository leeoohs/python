# 使用多个elif代码块

# 再多一个条件为65岁（含）以上的老人，可以半价（即5美元）
age = 20

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")