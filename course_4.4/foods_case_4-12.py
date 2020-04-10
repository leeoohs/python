# 在其中编写两个for循环，将各个食品列表都打印出来
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are")
for friend_food in friend_foods:
    print(friend_food)