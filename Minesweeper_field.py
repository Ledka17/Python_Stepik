n, m = [int(x) for x in input().split()]
a = ["." * (m+2)]
for i in range(n):
  a.append("." + input() + ".")
a.append("." * (m+2))
for i in range(1,n+1):
  for j in range(1,m+1):
    if a[i][j] == ".":
      print(sum(1 for x in (i-1, i, i+1) for y in (j-1, j, j+1) if a[x][y] == "*"), end='')
    else:
      print(a[i][j], end='')
  print()