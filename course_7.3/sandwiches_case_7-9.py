# 五香烟熏牛肉（pastrami）卖完了
sandwich_orders = ['cheese', 'pastrami', 'meat', 'pastrami', 'tomato', 'pastrami']
print(sandwich_orders)

print("Pastrami sold out!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)