# 序数 序数表示位置，如1st和2nd。在一个列表内存储1~9
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        print(str(number) + "st")
    elif number == 2:
        print(str(number) + "nd")
    else:
        print(str(number) + "th")
