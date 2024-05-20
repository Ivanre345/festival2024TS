import random

phones = []

for i in range(100):
    r = ['903', '916', '926', '968', '977']
    a = random.randint(0,4)


    b="".join([str(random.randint(0,9)),str(random.randint(0,9)),
               str(random.randint(0,9)),str(random.randint(0,9)),
               str(random.randint(0,9)),str(random.randint(0,9)),
               str(random.randint(0,9))])


    f = "+7" + str(r[a]) + b
    phones.append(f)
print(phones)
print(len(phones))


def found():
    found = input("Поиск ")
    for e in range(len(phones)):
        e -= 1
        if found in phones[e]:
            print(phones[e])


p903 = []
p916 = []
p926 = []
p968 = []
p977 = []

for i in range(len(phones)):
    i-=1

    if phones[i][2:5] == "903":
        p903.append(phones[i])

    elif phones[i][2:5] == "916":
        p916.append(phones[i])

    elif phones[i][2:5] == "926":
        p926.append(phones[i])

    elif phones[i][2:5] == "968":
        p968.append(phones[i])

    elif phones[i][2:5] == "977":
        p977.append(phones[i])

# print(p903)
# print(p916)
# print(p926)
# print(p968)
# print(p977)
# print(len(p903))
# print(len(p916))
# print(len(p926))
# print(len(p968))
# print(len(p977))



def sorting():
    phones2 = phones.copy()

    for i in range(len(phones2)):
        i-=1
        phones2[i]=int(phones2[i][1:])

    print(phones2)
    phones3 = sorted(phones2)
    print(phones3)
    for i in range(len(phones3)):
        phones3[i] = "+" + str(phones3[i])

    print(phones3)

def sorting2():
    for i in range(len(p903)):
        i-=1
        p903[i]=int(p903[i][1:])

    print(p903)
    phones3 = sorted(p903, reverse=True)
    print(phones3)
    for i in range(len(phones3)):
        phones3[i] = "+" + str(phones3[i])

    print(phones3)


    for i in range(len(p916)):
        i-=1
        p916[i]=int(p916[i][1:])

    print(p916)
    phones4 = sorted(p916, reverse=True)
    print(phones4)
    for i in range(len(phones4)):
        phones4[i] = "+" + str(phones4[i])

    print(phones4)

    for i in range(len(p926)):
        i-=1
        p926[i]=int(p926[i][1:])

    print(p926)
    phones5 = sorted(p926, reverse=True)
    print(phones5)
    for i in range(len(phones5)):
        phones5[i] = "+" + str(phones5[i])

    print(phones5)

    for i in range(len(p968)):
        i-=1
        p968[i]=int(p968[i][1:])

    print(p968)
    phones6 = sorted(p968, reverse=True)
    print(phones6)
    for i in range(len(phones6)):
        phones6[i] = "+" + str(phones6[i])

    print(phones6)


    for i in range(len(p977)):
        i-=1
        p977[i]=int(p977[i][1:])

    print(p977)
    phones7 = sorted(p977, reverse=True)
    print(phones7)
    for i in range(len(phones7)):
        phones7[i] = "+" + str(phones7[i])

    print(phones7)

    flaps = [','.join(phones3),','.join(phones4),','.join(phones5),','.join(phones6),','.join(phones7)]

    print(flaps)




sorting2()




















