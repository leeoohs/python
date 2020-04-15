# 编写一个程序，调查用户梦想的度假胜地

# 先创建一个空列表来存储梦想的度假胜地
dream_places = {}

# 创建一个标志，指出调查是否继续
ask_active = True

# 创建一个循环询问用户梦想胜地
while ask_active:
    name = input("Hello, what's you name? ")

    prompt = "If you could visit one place in the world, where would you go? "
    prompt += "\nEnter 'quit' to end the program. "
    place = input(prompt)

    if place == 'quit':
        print("Thank you!")
        ask_active = False
    else:
        # 将答卷存储到字典内
        dream_places[name] = place

        # 在询问是否还有人需参与调查
        repeat = input("Would you like to let another person respond? (yes/ no) ")

        if repeat == 'no':
            ask_active = False

print("\n--- Poll Results ---")
for name,place in dream_places.items():
    print(name.title() + "'s dream place is " + place)


