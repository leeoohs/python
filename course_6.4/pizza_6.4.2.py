# 在字典红存储列表

# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    # toppings的值是一个列表，其中存储了顾客要求添加的所有配料
    'toppings': ['mushroom', 'extra cheese']
    }

# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

# for循环访问了配料列表，用了键'toppings'python将从字典中提取配料列表
for topping in pizza['toppings']:
    print("\t" + topping)

# 另一个例子
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        print("\n" + name.title() + "'s favorite language is:")
        print("\t" + languages[0])
