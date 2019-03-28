d = {}
for i in input().split():
    key = len(i)
    if key not in d.keys():
        d[key] = 1
    else:
        d[key] += 1
for i in sorted(d.keys()):
    print(str(i)+': '+str(d[i]))