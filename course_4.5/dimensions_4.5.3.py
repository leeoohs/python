# 修改元组变量

# 虽然不能修改元组的元素，但可以给存储元组的变量赋值
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

# 将一个新元组存储到变量dimensions中，并打印出来
dimensions = (400, 100)
print("\nModifiend dimensions:")
for dimension in dimensions:
    print(dimension)