# 用户简介：调用函数是创建有关于我的简介
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('shan', 'huang',
                             location='nanning',
                             field='tumugonghceng',
                             age=28)
print(user_profile)