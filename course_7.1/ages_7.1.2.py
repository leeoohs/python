# 使用int()来获取数值输入
# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age
# '21'

"""用户输入的数字21，但我们请求python提供变量age的值时，它返回的是'21'——
用户输入的数字的字符串表示。我们怎么知道python将输入解读成了字符串呢？
因为这个数字用引号括起来了。如果我们只想打印输入，这一点问题都没有，
但如果你试图将输入作为数字使用，就会引发错误"""

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age > 18
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: '>' not supported between instances of 'str' and 'int'

'''你试图将输入用于数值比较时，python会引发错误，因为它无法将字符串和证书进行比较：
不能讲存储在age中的字符串'21'与数值18进行比较。
为了解决这个问题，可使用函数int()，它让python将输入视为数值。
函数int()将数字的字符串表示转换为数值表示'''

# >>> age = input("How old are you? ")
# How old are you? 21
# >>> age = int(age)
# >>> age >= 18
# True
