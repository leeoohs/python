# 返回值：函数并非直接显示输出，相反，它可以处理一些数据，并返回一个或一组值
# 在函数中，可使用return语句将值返回到调用函数的代码行
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    # 将结果返回到函数中调用
    return full_name.title()


# 调用返回值的函数时，需要提供一个变量用于存储返回的值。
# 这里将返回值存储在了变量musician中了
musician = get_formatted_name('jimi', 'hendrix')
print(musician)