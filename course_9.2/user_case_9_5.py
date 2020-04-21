# 尝试登录次数，添加一个名为login_attempts的属性。
# 编写一个名为increment_login_attempts()的方法，它将属性login_attempts的值加1。
# 再编写一个名为reset_login_attempts()的方法，它将属性login_aiiempts的值重置为0。
class User():
    """模拟创建一个用户简介"""
    def __init__(self, first_name, last_name, location, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.age = age
        self.full_name = first_name + last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.full_name.title() + " comes from " + self.location)
        print("He/She is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Everybady say hello to " + self.full_name.title() + ".")

    def login_attempt(self):
        print("尝试登录" + str(self.login_attempts) + "次了。")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0



user = User('kai', 'liu', 'tianjin', 22)
print(user.full_name)
print(user.first_name + " " + user.last_name)
print(user.location)
print(str(user.age))

user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.login_attempt()

user.increment_login_attempts()
user.login_attempt()

user.reset_login_attempts()
user.login_attempt()
