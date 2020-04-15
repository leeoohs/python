# 向函数传递信息

"""只需稍作修改，就可以让函数greet_user()不仅向用户显示Hello!,
还将用户的名字用作抬头。为此，可在函数定义def greet_user()的括号内添加username。
通过在这里添加username，就可让函数接受你给username指定的任何值。"""

# 现在这个函数要求你调用它时给username指定一个值。调用greet_user()时，可将一个名字传递给它
def greet_user(username):
    print("Hello, " + username.title() + "!")


"""代码greet_user('jesse')调用函数greet_user()，
并向它提供执行print语句所需要的信息。这个函数接受你传递给它的名字"""
greet_user('jesse')
greet_user('sarah')