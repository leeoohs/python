# if-elif-else结构，检查超过两个的情形，可使用该结构

# 游乐场收费标准：4岁以下免费；4~18岁收费5美元；18岁（含）以上收费10美元
age = 12

if age < 4:
    print("Your admission cost is $o.")
# elif是另一个if测试，它仅在前面的测试未通过时才会运行
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $1o.")

# 为了让代码更简洁，可在最后面添加一条简单的print语句
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
else:
    price = 10

print("Your admission cost is $" + str(price) + ".")