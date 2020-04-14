# 创建一个字典，将三个人的名字作为键，对于每个人都存储他喜欢的1~3个地方
favorite_places = {
    'daxian': ['tiananmen', 'gugong', 'xuanwumen'],
    'kaige': ['home'],
    'xiaohai': ['beijing', 'shanghai', 'hongkong'],
    'ayan': ['xinjiapo', 'aomen'],
    }

for name, places in favorite_places.items():
    if len(places) > 1:
        print(name.title() + "'s favorite places are:")
        for place in places:
            print("\t" + place)
    else:
        print(name.title() + "'s favorite place is:")
        print("\t" + places[0])