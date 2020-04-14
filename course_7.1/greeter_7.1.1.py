# 编写清晰的程序
# 每当使用函数input()时，都应指定清晰而易于明白的提示，准确地指出你希望用户提供什么样的信息

# 通过在提示末尾包含一个空格，可将提示语用户输入分开
name = input("Please enter your name: ")
print("Hello, " + name + "!")



# 有的时候提示超过一行，可将提示存储在一个变量中，再将变量传递给函数input()
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# 使用函数input()时，python将用户输入解读为字符串