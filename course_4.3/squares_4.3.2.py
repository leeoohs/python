# 在python中，两个星号（**）表示乘方运算

# 将前10个整数的平方加入到一个列表中
# 首先创建一个空列表
squares = []
# 使用函数range()让python遍历1~10的值
for value in range(1,11):
    # 在循环中，计算当前值的平方，并将结果存储到变量square中
    square = value**2
    # 将新计算的得到的平方值附加到列表squares末尾
    squares.append(square)

print(squares)


# 为了让这些代码更简洁，可不使用临时变量square，而直接将每个计算得到的值附加到列表末尾
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)
# 打印列表内最小值
print(min(squares))
# 打印列表内最大值
print(max(squares))
# 打印列表数总和
print(sum(squares))