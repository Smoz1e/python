messege  = ['Привет','Поока','Как дела?','Понятно','Ясно']
messege2 = []

def send_messedge(maseedg, send):
    # print(maseedg)
    while maseedg:
        n = maseedg.pop()
        # print(n)
        send.append(n)

def printe(mesedg):
    for i in mesedg:
        print(i)

send_messedge(messege[:], messege2)
print(messege)
printe(messege2)

        