# 用户：
class User():
    """模拟创建一个用户简介"""

    def __init__(self, first_name, last_name, locatioan, age):
        self.first_name = first_name
        self.last_name = last_name
        self.location = locatioan
        self.age = age
        self.full_name = self.first_name + self.last_name

    def describe_user(self):
        print(self.full_name.title() + " comes from " + self.location)
        print("He/She is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Everybady say hello to " + self.full_name.title() + ".")


user = User('kai', 'liu', 'tianjin', 22)
print(user.full_name)
print(user.first_name + " " + user.last_name)
print(user.location)
print(str(user.age))

user.describe_user()
user.greet_user()
