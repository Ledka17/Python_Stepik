def fractd(n,m):
    if n != 1:
      if m!=0:
        print(n//m, end=' ')
        fractd(m, n % m)

n,m = [int(i) for i in input().split('/')]
fractd(n,m)