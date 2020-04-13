# 测试多个条件

'''if-elif-else结构功能强大，但仅适合用于ZHi有一个条件满足的情况：
遇到通过了的测试后，python就跳过余下的测试。
然而，有时候必须检查你关心的所有条件。
在这种情况下，应使用一系列不包含elif和else代码块的简单if语句。
在可能有多个条件为Ture，且你需要在每个条件为Ture是都采用相应措施时，使用这种方法。'''

requested_toppings = ['mushrooms', 'extra cheese']

# 检查顾客是否点了配料'mushroom'，如果点了，就打印一条确认消息
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
# 该处为一个简单的if语句，而不是elif或else语句，因此不管前一个测试是否通过，都将进行这个测试
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

# 转换成if-elif-else语句，代码将不能正确地运行，因为有一个测试通过，就会跳过剩余测试
requested_toppings = ['mushrooms', 'extra cheese']

# 检查顾客是否点了配料'mushroom'，如果点了，就打印一条确认消息
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
# 该处为一个简单的if语句，而不是elif或else语句，因此不管前一个测试是否通过，都将进行这个测试
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")