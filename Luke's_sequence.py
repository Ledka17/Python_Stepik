def luka(L0, L1, n):
    if n == 0:
        return L0
    elif n == 1:
        return L1
    else:
        for i in range(2,n+1):
            s = L0 + L1
            L0, L1 = L1, s
        return s

L0, L1, n = [int(i) for i in input().split()]
print(luka(L0, L1, n))