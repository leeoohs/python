# 让用户选择何时退出
# 我们在程序中定义了一个退出值，只要用户输入的不是这个值，程序就接着运行
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# 设置变量message的初始值，首次执行while代码行时有可供检查的东西
# 如果没有可供比较的东西，python将无法继续运行程序
message = ""
while message != 'quit':
    message = input(prompt)

    # 用户输入不为'quit'时打印message
    if message != 'quit':
        print(message)