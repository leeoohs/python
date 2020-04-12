# 省略else代码块

"""python并不要求if—elif结构后面必须有else代码块，
在有些情况下，else代码块很有用；
而在其他一些情况下，使用一条elif语句来处理特定的情形更清晰"""

age = 20

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
# 这样的表示比else代码更清晰些
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")