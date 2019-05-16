a = [i for i in input().split()]
m = {}
for i in a:
    if i.lower() not in m:
        m[i.lower()] = 1
    else:
        m[i.lower()] += 1 
for key,value in m.items():
    print(key,value)