# 将pizza存储到变量friend_pizza中
pizzas = ['seafood pizza', 'beef pizza', 'corn pizza']
friend_pizzas = pizzas[:]

# 在原来的比萨列表中添加一种pizza
pizzas.append('egg pizza')

# 在列表friend_pizzas列表中添加另一种比萨
friend_pizzas.append('sausage pizza')

# 核实你有两个不同的列表，并打印"My favorite pizzas are:"，再使用一个for循环来打印第一个列表
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)


# 打印消息"My friend's favorite pizzas are:",再使用一个for循环来打印第二个列表
print("\nMy friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)