# 创建一个应该会接受调查的人员名单
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

users = ['jen', 'bill', 'sarah', 'sam', 'bob']

for user in users:
    if user in [name for name in favorite_languages.keys()]:
        print(user.title() + ", thank you for taking the poll.")
    else:
        print("Sorry,please take our poll!")

