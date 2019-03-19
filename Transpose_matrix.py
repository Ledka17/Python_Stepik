n,m = [int(i) for i in input().split()]
s = []
for i in range(n):
    s.append(input().split())
for  j in range(m):
    for i in range(n):
        print(s[i][j], end=' ')
    print()