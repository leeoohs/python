# 使用break退出循环,在任何python循环中都可使用break语句。


"""要立即退出while循环，不再运行循环中余下的代码，也不管条件测试的结果如何，
可使用break语句。break语句用于控制程序流程，可使用它来控制哪些代码行将执行，
哪些代码行不执行，从而让程序按你的要求执行你的要执行的代码。"""

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
