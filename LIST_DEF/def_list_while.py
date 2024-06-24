def func_print(not_ready,  ready):
    while not_ready:
        sready = not_ready.pop()
        # print(sready)
        ready.append(sready)
        # print(ready)

def models(model):
    for i in model:
        print(i)

list1=['Mod1','Mod2','Mode3','Mode4',]
list2=[]
func_print(list1, list2)

models(list2)

