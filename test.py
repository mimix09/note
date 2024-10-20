# add (co zrobic, *info)
# del (id)
# reset
# stage (id, stan)

x = "del myster white yo"

tab = ["add", "del", "reset", "stage"]

t = ""
u = 0
for i in tab:
    q = 0
    print("---")
    for j in range(len(i)):
        print(x[j] + " - " + i[j])
        if x[j] == i[j]:
            q += 1

    if q == len(i):
        t = i
        u = q+1

print("--")
print(x[u:])