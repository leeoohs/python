# 假设在游戏中射杀了一个外星人，请创建一个名为alien_color的变量
alien_color = ['green', 'yellow', 'red']

# 编写一条if语句，检查外星人是否是绿色的；如果是就打印一条消息
if 'green' in alien_color:
    print("You are getting 5 integral.")

# 编一个if-else结构
alien_color = ['green', 'yellow', 'red']

if 'green' not in alien_color:
    print("You are getting 10 integral.")
else:
    print("You are getting 5 integral")

# 另一个版本
alien_color = ['green', 'yellow', 'red']

if 'green' in alien_color:
    print("You are getting 5 integral.")
else:
    print("You are getting 10 integral")

# 编一个if-elif-else结构,绿色
alien_color = ['green', 'yellow', 'red']

# 如果外星人是绿色，就打印一条消息获得5点积分
if 'green' in alien_color:
    print("You are getting 5 integral.")
# 如果外星人是黄色，就打印一条消息获得10点积分
elif 'yellow' in alien_color:
    print("You are getting 10 integral.")
# 如果外箱人是红色，就打印一条消息获得15点积分
else:
    print("You are getting 15 integral.")

# 黄色
alien_color = ['green', 'yellow', 'red']

if 'yellow' in alien_color:
    print("You are getting 10 integral.")
elif 'green' in alien_color:
    print("You are getting 5 integral.")
else:
    print("You are getting 15 integral.")

# 红色
alien_color = ['green', 'yellow', 'red']

if 'red' in alien_color:
    print("You are getting 15 integral.")
elif 'yellow' in alien_color:
    print("You are getting 10 integral.")
else:
    print("You are getting 5 integral.")
