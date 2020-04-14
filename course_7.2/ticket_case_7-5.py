# 电影票：不到3岁的观众免费；3~12岁的观众为10美元；超过12岁的观众为15美元
# 编写一个循环，询问用户的年龄
age = input("How old are you? ")
age = int(age)

while True:
    if age < 3:
        print("\nThe ticket is for free.")
        break
    elif age < 12:
        print("\nTicket $10.")
        break
    else:
        print("\nTicket $15.")
        break