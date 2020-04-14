favorite_numbers = {
    'liukai': [3, 5, 10],
    'lixiaohua': [6, 8, 2],
    'lishaoyan': [7],
    'xiaohai': [8, 22],
    'daxian': [7, 3],
    }

for name, numbers in favorite_numbers.items():
    if len(numbers) > 1:
        print(name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + str(number))
    else:
        print(name.title() + "'s favorite number is:")
        print("\t" + str(numbers[0]))

