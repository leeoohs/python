# 将其中的一系列print语句替换为一个遍历字典中键和值的循环
vocabularys = {
    'for': '循环',
    'if': '条件测试',
    'elif': '另一个if',
    'print': '打印',
    'del': '删除',
    }

for name, definition in vocabularys.items():
    print(name.title() + ":\n" + definition)