# for循环结束后执行一些操作

# 在for循环后面，没有缩进的代码都只执行一次，而不会重复执行。

# 打印一条向全体魔术师的致谢消息，需要将相应对的代码放在for循环后面，且不缩进
magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")

print("Thank you,everyone.That was a great magic show!")
