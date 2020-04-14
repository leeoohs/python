# 询问用户有多少人用餐，如果超过8人，就打印一条消息说没有空桌了
booking = input("How many of you have dinner? ")
booking = int(booking)

if booking > 8:
    print("Sorry, we don't have enough seats!")
else:
    print("OK, welcome in.")