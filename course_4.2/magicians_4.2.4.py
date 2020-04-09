# 循环后不必要的缩进
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ",that was a great trick!")
    print("I can't wait to see your next trick," + magician.title() + ".\n")

    print("Thank you,everyone.That was a great magic show!")

# 执行结果如下：
'''Alice,that was a great trick!
I can't wait to see your next trick,Alice.

Thank you,everyone.That was a great magic show!
David,that was a great trick!
I can't wait to see your next trick,David.

Thank you,everyone.That was a great magic show!
Carolina,that was a great trick!
I can't wait to see your next trick,Carolina.

Thank you,everyone.That was a great magic show!'''
# 由于第三个print语句被缩进，它将针对列表中的每位魔术师执行一次
