list1 = ['R','D','F']
list2 = []

while list1:
    peremen = list1.pop()
    list2.append(peremen)

print(f'Сейчас мы вывмдем список {list2}')

for list3 in list2:
    print(f'Выводим в строку {list3}')