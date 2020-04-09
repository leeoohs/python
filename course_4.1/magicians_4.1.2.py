# 在for循环中执行更多的操作

# 对于每位魔术师，都打印一条消息，指出他的表演很精彩
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")

'''这个循环第一次迭代时变量magician的值为alice，因此python打印的第一条消息的抬头为Alice，
这个循环第二次迭代时变量magician的值为david，因此python打印的第一条消息的抬头为David，
这个循环第三次迭代时变量magician的值为carolina，因此python打印的第一条消息的抬头为Carolina。'''

# 在for循环中，想包含多少行代码都可以。在代码行for magician in magicians后面，每个缩进的代码行都是循环的一部分，且将针对列表中的每个值都执行一次
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")
