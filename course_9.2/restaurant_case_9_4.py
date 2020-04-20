# 就餐人数，添加一个number_served的属性，并将其默认值设置为0
# 根据这个类创建一个名为restaurant的实例
class Restaurant():
    def __init__(self, restaurant_name, cuisine_tpye):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_tpye
        self.number_served = 0

    def describe_restaurant(self):
        print("Our restaurant name is " + self.restaurant_name.title() + ".")
        print("We are a " + self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is in business")

    def set_number_served(self):
        print("We have " + str(self.number_served) + " peoples in restaurant.")

    def update_set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, numbers):
        self.number_served += numbers


restaurant = Restaurant('qianxihe', 'zhongcanting')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.number_served = 23
restaurant.set_number_served()

restaurant.update_set_number_served(26)
restaurant.set_number_served()

restaurant.increment_number_served(5)
restaurant.set_number_served()


