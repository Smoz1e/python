list1 = ['Привет','Пока','Как дела?','Давай','Сюда']
list2 = []

def senf(mesedge, send):
    while mesedge:
        n = mesedge.pop()
        send.append(n)

def prints(new_mesedg):
    for i in new_mesedg:
        print(i)

senf(list1[:], list2)

prints(list1)
print('---------------------')
prints(list2)

