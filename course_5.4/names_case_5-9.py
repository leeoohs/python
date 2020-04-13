# 处理没有用户的情形
names = ['admin', 'sam', 'tom', 'amily', 'bill', 'leo']

if names:
    for name in names:
        if name == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hello " + name +",thank you for logging in again.")
else:
    print("We need to find some users!")