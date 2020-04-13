# 以特殊方式跟管理员打招呼

# 创建一个至少包含5个用户名的列表，且其中一个用户名为'admin'
names = ['admin', 'sam', 'tom', 'amily', 'bill', 'leo']

# 遍历用户名列表，如果用户名为'admin'就打印一条特殊的问候
for name in names:
    if name == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hello " + name +",thank you for logging in again.")