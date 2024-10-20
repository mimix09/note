# ┘ ✓
# C:\Users\mpian\Desktop\To do lista

# 1_x_Nazwa_opis
# 2_+_Nazwa_opis2
# 3_x_NazwaKolejna

print("Notatnik")

tab = []
komenda = ""

def wyswietlanie():
    wyjscie = ""
    for i in tab:
        for j in range(len(i)):
            if j < len(i)-1 and j != 0 and j < 2:
                wyjscie += i[j] + "|"
            elif j == 0:
                wyjscie += i[0] + ".|"
            elif j > 1 and j < len(i)-1:
                wyjscie += i[j] + " - "
            else:
                wyjscie += i[j]
        wyjscie += "\n"

    print(wyjscie)

def pobieranie():
    file = open('todo.txt', 'r')
    text = file.read()

    if text != '':
        array = []
        array = text.split("\n")
        for x in array:
            tab.append(x.split("_"))

def dodawanie(dane):
    p = dane.split(", ")
    p.insert(0, str(len(tab)+1))
    tab.append(p)

def usuwanie(us):
    # usuwanie
    tab.pop(us-1)
    
    #podmienianie numerow
    for i in range(len(tab)):
        tab[i][0] = str(i+1)

def reset():
    tab.clear()

def zapis():
    result = "";
    i = 0

    print(tab)
    for x in tab:
        for y in range(len(x)):
            if y < len(x)-1:
                result += x[y] + "_"
            else:
                result += x[y]
        if i < len(tab)-1:
            result += "\n"
        i += 1

    file = open('todo.txt', 'w')
    file.write(result)

# add (co zrobic, *info)
# del (id)
# reset
# stage (id, stan)

def sekfencja():
    pass

def wpisywanie():
    odp = input("X: ")

    quest = ["add", "del", "reset", "stage"]
    t = ""
    result = ""

    for i in quest:
        q = 0
        for j in range(len(i)):
            if odp[j] == i[j]:
                q += 1

        if q == len(i):
            t = i
            result = odp[q+1:]
    
    print(result)

    if t == quest[0]: # add
        dodawanie(result)
    elif t == quest[1]: # del
        pass
    elif t == quest[2]: # reset
        pass
    elif t == quest[3]: # stage
        pass
    else:
        print("nie ma takiej komendy")

wpisywanie()