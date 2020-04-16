# 编写一个city_country()的函数，接受成型名称及其所属的国家
def city_country(city_name, country):
    city = '"' + city_name + ', ' +country + '"'
    return city.title()


city_0 = city_country('beijing', 'china')
print(city_0)
city_1 = city_country('tianjin', 'china')
print(city_1)
city_2 = city_country('new york', 'america')
print(city_2)

