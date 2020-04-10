# 元组

# python将不能修改的值成为不可变的，而不可变的列表被称为元组

# 元组看起来犹如列表，但使用圆括号而不是方括号来标识

# 如有一个人大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的
# 首先定义了元组dimension
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# 尝试修改元组中的一个元素
dimensions = (200, 50)
dimensions[0] = 250

# 执行结果如下：
'''Traceback (most recent call last):
  File "/Users/huangdaxianer./Downloads/subline/project/course_4.5/dimensions_4.5.1.py", line 16, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment'''
