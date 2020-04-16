# 餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性
class Restaurant():
    def __init__(self, restaurant_name, cuisine_tpye):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_tpye

    def describe_restaurant(self):
        print("Our restaurant name is " + self.restaurant_name.title() + ".")
        print("We are a " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is in business")


restaurant_0 = Restaurant('qianxihe', 'zhongcanting')
restaurant_1 = Restaurant('kaigefandian', 'zhongcanting')
restaurant_2 = Restaurant('shanjiefandian', 'xicanting')



print(restaurant_0.restaurant_name)
print(restaurant_0.cuisine_type)

restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

print("\n" + restaurant_1.restaurant_name)
print(restaurant_1.cuisine_type)

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()

print("\n" + restaurant_2.restaurant_name)
print(restaurant_2.cuisine_type)

restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()




