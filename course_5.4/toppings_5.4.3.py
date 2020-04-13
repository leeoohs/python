# 使用多个列表

# 定义两个列表，其中一个列表包含比萨店供应的配料，另一个包含顾客点的配料
available_toppings = ['mushroom', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushroon', 'french fries', 'extra cheese']

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("Adding " + requested_topping + ".")
        else:
            print("Sorry,we don't have " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")

print("\nFinished making your pizza!")