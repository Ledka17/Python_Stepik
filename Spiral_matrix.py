n = int(input())
a = [[0]*n for i in range(n)]
k = 1
i = 0
j = 0
while k<= n**2:
    while j<n and a[i][j] == 0:
        a[i][j] = k
        k +=1
        j +=1
    j -=1
    i +=1
    while i<n and a[i][j] == 0:
        a[i][j] = k
        k +=1
        i +=1
    i -=1
    j -=1
    while j>=0 and a[i][j] == 0:
        a[i][j] = k
        k +=1
        j -=1
    j +=1
    i -=1
    while i>=0 and a[i][j] == 0:
        a[i][j] = k
        k +=1
        i -=1
    i +=1
    j +=1
for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")
    print()