# 使用if语句处理列表

# 检查特殊元素，创建一个表，使用循环来指出添加到披萨中的配料
requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    # 如果比萨店的请教用完了，可在for循环中包含一条if语句
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")

