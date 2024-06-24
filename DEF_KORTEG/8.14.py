def car_user(proizvod, name_model, **element):
    element['proiz'] = proizvod
    element['mod'] = name_model
    return element

car = car_user('BMW','M8', color = 'blue',)
for key, value in car.items():

    print(key, value)

print('-----------------')

for name in car.values():
    print(name)