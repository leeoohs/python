# 忘记缩进额外的代码行
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
print("I can't wait to see your next trick," + magician.title() + ".\n")


# 执行结果如下：
'''Alice,that was a great trick!
David,that was a great trick!
Carolina,that was a great trick!
I can't wait to see your next trick,Carolina.'''

'''最终的结果是，对于列表中的每位魔术师，都执行了第一条print语句，因为它缩进了；
而第二条print语句没有缩进，因此它只在循环结束后执行一次。
由于变量magician的终值为'carolina'，因此只有她收到了消息"I can't wait to see your next trick,Carolina."'''