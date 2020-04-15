# 创建一个包含各种三明治的列表
sandwich_orders = ['cheese sandwich', 'meat sandwich', 'tomato sandwich']

# 再创建一个名为finished_sandwiches的空列表
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich)
    finished_sandwiches.append(current_sandwich)

print("\nni dian de san ming zhi wei: ")
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
