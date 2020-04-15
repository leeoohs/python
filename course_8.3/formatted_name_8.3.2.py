# 让实参变成可选的，可使用默认值来让实参变成可选的
# 为了让中间名变成可选的，可给形参middle_name指定一个默认值——-空字符串
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    # 检查是否提供了中间名，if middle_name：（python将非空字符串解读为True）
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

musician = get_formatted_name('shan', 'huang')
print(musician)