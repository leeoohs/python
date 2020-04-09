# 遗漏了冒号

# for语句末尾的冒号告诉python，下一行是循环的第一行
"""magicians = ['alice', 'david', 'carolina']
for magician in magicians
    print(magician)"""

# 执行结果如下：
'''  File "/Users/huangdaxianer./Downloads/subline/project/course_4.2/magicians_4.2.5.py", line 5
    for magician in magicians
                            ^
SyntaxError: invalid syntax'''

'''如果你不小心遗漏的冒号，将导致语法错误，因为python不知道你的意欲何为。
这种错误虽然易于消除，但是并不那么容易发现。'''