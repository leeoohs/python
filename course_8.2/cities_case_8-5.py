# 编写一个describe_city()函数，接受一座城市的名字以及所属国家
def describe_city(city_name, country='china'):
    print(city_name.title() + " is in " + country.title())


describe_city('tianjin')
describe_city(city_name='beijing')
describe_city('new york', 'america')
describe_city(city_name='new york', country='america')
describe_city(country='american', city_name='new york')