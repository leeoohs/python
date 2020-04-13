# 遍历字典，遍历所有键-值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

# for语句的第二部分包含字典名和方法items()，它饭就一个键-值对列表
# for循环依次将每个键-值对存储到指定的两个变量中
for key,value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

# 注意：几遍遍历字典时，键-值对的返回顺序也与存储顺序不同
# python不关心键-值得存储顺序，值跟踪键和值之间的关联关系

avorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name,language in avorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")