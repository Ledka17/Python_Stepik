n, m = [int(x) for x in input().split()]
a = []
for i in range(n):
    s = input()
    a.append(s[len(s)-1]+s+s[0])
a.append(a[0])
a.insert(0, a[len(a)-2])
print(a)
for i in range(1,n+1):
    for j in range(1,m+1):
        ch = sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if a[x][y] == "X")
        if a[i][j] == '.':
            print('X' if ch == 3 else '.', end='')
        else:
            print('X' if ch == 4 or ch == 3 else '.', end='')
    print()