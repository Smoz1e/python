def userse(user, *info):
    print(user)
    for i in info:
        print(i)

def add(user, passw, *info):
    print(user)
    print(passw)
    for i in info:
        print(i)

def user_info(name, sorname, **info):
    info['Name'] = name
    info['sorname'] = sorname
    for kye, v in info.items():
        print(kye,':',v)