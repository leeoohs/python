# 10的整数倍：让用户输入一个数字，并指出这个十足是否是10的整数倍
number = input("Please enter a number: ")
number = int(number)

if number % 10 == 0:
    print("\nThe number " + str(number) + " is an intergral muitiple of 10.")
else:
    print("\nThe number " + str(number) + " is not an intergral muitiple of 10.")