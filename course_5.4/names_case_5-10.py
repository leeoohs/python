# 检查用户名

# 创建一个列表命名为current_users，包含5个用户名
current_users = ['admin', 'Sam', 'tom', 'amily', 'bill', 'leo']

# 创建一个列表名为new_users,并确保其中一个有一两个用户名也包含在current_users内
new_users = ['sam', 'bob', 'tom', 'saly', 'eric']


for new_user in new_users:
    # 确保比较时不区分大小写
    if new_user.lower() in [current_user.lower() for current_user in current_users]:
        print(new_user.title() + " is exist，you have to change.")
    else:
        print("User name not enabled.")
