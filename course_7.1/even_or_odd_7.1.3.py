# 求模运算符
# 处理数值信息时，求模运算符（%）是一个很有用的工具，他将两个数相除并返回余数：
# >>> 4 % 3
# 1
# >>> 5 % 3
# 2
# >>> 6 % 3
# 0
# >>> 7 % 3
# 1

"""求模运算符不会指出一个数是另一个数的多少倍，而只出余数是多少。
如果一个数可被另一个数整除，余数就为0，因此求模运算符将返回0。"""

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")
