# 使用标志

"""在要求很多条件都满足才继续运行的程序中，可定义一个变量，
用于判断整个程序是否处于活动状态。这个变量被称为标志，充当了程序的交通信号灯。
你可让程序在标志位True时继续运行，并在任何事件导致表示的值为false时让程序停止运行。
这样while语句中就指只需检查一个条件————标志的当前值是否未True，并将所有测试
（是否发生了应将标志设置为False的时间）都放在其他地方，从为让程序变更为整洁。"""

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# 命名一个标志为active
active = True
while active:
    message = input(prompt)

    # 用户输入不为'quit'时打印message
    if message == 'quit':
        active = False
    else:
        print(message)