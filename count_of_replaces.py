s,a,b = input(), input(), input()
if a == b and a not in s:
    print(0)
else:
    i = 0
    while s.find(a) != -1:
        s = s.replace(a,b)
        i += 1
        if i > 1000:
            break
    if i <= 1000:
        print(i)
    else:
        print("Impossible")