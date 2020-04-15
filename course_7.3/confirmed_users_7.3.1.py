# 使用while循环来处理列表和字典

"""for循环是一种遍历列表的额有效方式，但在for巡检中不应修改列表，否则将导致python
难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。通过
将while循环同列表和字典结合起来使用，可手机、存储并组织大量输入，共以后查看和显示。"""

# 在列表之间移动元素
# 验证用户的同时将其从未验证用户列表提取出来，再将其加入另一个已验证用户列表中。


# 首先，创建一个带验证用户列表
# 和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
condirmed_users = []

# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
# while循环将不断地运行，直到unconfirmed_users列表变成空的
while unconfirmed_users:
    # 方法pop()以每次一个的方式从列表unconfirmed_users末尾删除未验证的用户。
    current_users = unconfirmed_users.pop()

    print("verifying user: " + current_users.title())
    condirmed_users.append(current_users)

# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for condirmed_user in condirmed_users:
    print(condirmed_user.title())