# 创建一个字典，其中将三个城市用做键，对于每座城市都创建一个字典
cities = {
    'beijing': {
        'country': 'china',
        'population': '1 bollion 400 million',
        'fact': 'capital',
        },

    'washinton': {
        'country': 'America',
        'population': '600 million',
        'fact': 'statue of liberty',
        },


    'tianjin': {
        'country': 'china',
        'population': '50 million',
        'fact': 'municipality directly under the central government'
        },

    }

for city, city_info in cities.items():
    print("\nCity name: " + city.title())

    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print("Country: " + country.title())
    print("Population: " + population)
    print("Fact: " + fact.title())