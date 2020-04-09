# 不必要的缩进

# 如果你不小心缩进了无需缩进的代码行，python将指出这一点：
"""message = "Hello Python world!"
    print(message)"""


# print语句无需缩进，因为它不属于前一行代码，因此执行结果如下：
'''  File "/Users/huangdaxianer./Downloads/subline/project/course_4.2/hello_world_4.2.3.py", line 5
    print(message)
    ^
IndentationError: unexpected indent'''