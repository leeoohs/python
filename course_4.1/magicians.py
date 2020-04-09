# 使用for循环来打印列表内所有的元素


"""magicians = ['alice','david','carolina']
for magician in magicians:
    print(magician) """

# 定义一个魔术师名称列表（1）
magicians = ['alice', 'david', 'carolina']
# 定义一个for循环，让python从列表magicians中取出一个名字，并将其存储在变量magician中（2）
for magician in magicians:
    # 让python打印前面存储到变量magician中的名字（3）
    print(magician)

'''这样，对于列表中的每个名字，python都将重复执行（2）和（3）出的代码行。对列表中的每个元素，都将执行循环指定的步骤，
而不管列表包含多少个元素。如果列表包含一百万个元素，python就重复执行指定的步骤一百万次，且通常速度非常快.'''
