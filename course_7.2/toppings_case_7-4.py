# 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环
prompt = "\nPlesae enter the toppings of pizza."
prompt += "\n(Enter 'quit' to end the program.) "

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        print("\nFinished making your pizza!")
    else:
        print(toppings)