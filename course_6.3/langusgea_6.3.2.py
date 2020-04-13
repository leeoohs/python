# 遍历字典中的所有键
# 在不需要使用字典中的值时，可使用方法keys()

avorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 让python提取字段中的所有键，并依次存储到变量name中
for name in avorite_languages.keys():
    print(name.title())
# 与上述输出相同
for name in avorite_languages:
    print(name.title())

# 指出两位朋友虚幻的语言
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " +
              # 将变量name当做值作为键
              favorite_languages[name].title() + "!")

# 还可以使用keys()确定某个人是否接受了调查
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

'''方法keys()并非只能用于遍历，实际上，它返回一个列表，其中包含字典中的所有键，
因此可以核实'erin'是否包含在列表中，不包含则打印一段消息'''
