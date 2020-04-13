# 创建一个字典，在其中存储三条大河流及其流经国家
rivers = {
    'danube': 'austria',
    'nile': 'egypt',
    'lancang river': 'china',
    }

for name, city in rivers.items():
    print("The " + name.title() +
          " runs through " + city.title() +
          ".")

for name in rivers.keys():
    print(name.title())

for city in rivers.values():
    print(city.title())