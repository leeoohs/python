# 在循环中使用continue

"""要返回到循环开头，并根据条件测试结构决定是否继续执行循环，
可使用continue语句，它不像break语句那样不再执行余下的代码并退出整个循环。"""

current_number = 0
while current_number < 10:
    current_number += 1

    # 如果能被2整除，就执行continue语句，让python忽略余下的代码，并返回到循环的开头。
    # 如果当前的数字不能被2整除，就执行循环中余下的代码，python将这个数字打印出来
    if current_number % 2 == 0:
        continue

    print(current_number)
