# 汽车
def build_car(manufacturer, model, **car_info):
    cars = {}
    cars['zhizaoshang'] = manufacturer
    cars['xinghao'] = model
    for key, value in car_info.items():
        cars[key] = value
    return cars


che = build_car('subaru', 'outback',
                color='blue',
                fitting_parts='door',
                years=1986)
print(che)