# while循环
# for循环用于珍贵极合中的每个元素的一个代码块，而while循环不短地运行，直到指定的条件不满足为止

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

'''在第一行，我们将current_number设置为1，从而指定从1开始数。
接下来的while循环被设置成这样：只要current_number小于或等于5，
就直接巡行这个循环。循环中的代码打印current_number的值，
再使用代码current_number += 1（代码current_number = current_number + 1的简写）
将其值加1。只要满足条件current_number <= 5，python就接着运行这个循环。'''