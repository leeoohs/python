# 使用任意数量的关键字实参
"""有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。
在这种情况下，可将函数编写能够接受任意数量的键-值对————调用语句提供了多少就接受多少。"""

# 形参**user_info中的两个星号让python创建一个名为useer_info的空字典
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)