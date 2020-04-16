# 传递列表
"""你经常会发现，向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象
（如字典）。将列表传递给函数后幂函数就能直接访问其内容。"""

# 假设有一个用户列表，我们要问候其中的每位用户。
# 下面的示例将一个名字列表传递给一个名为greet_user()的函数
def greet_user(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


"""我们将greet_user()定义成接受一个名字列表，并将其存储在形参names中。
这个函数遍历收到的列表，并对其中的每位用户都打印一条问候语。
因此我们定义了一个用户列表————usernames，然后调用greet_user()，
并将这个列表传递给它"""
usernames = ['hannah', 'tyr', 'margot']
greet_user(usernames)

