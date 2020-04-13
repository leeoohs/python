# 由类似对象组成的字典
# 字典也可用来存储众多对象的同一种信息
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# 在最后一个键-值对后面也加上逗号，为以后在下一行添加键-值对做好准备

'''注意：对于较长的列表和字典，大多数编辑器都有以类似方式设置其格式的功能。
对于较长的字典，还有其他一些可行的格式设置方式，因此在你的编辑器或其他源代码码中，
你可能会看到稍微不同的格式设置方式。'''

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")