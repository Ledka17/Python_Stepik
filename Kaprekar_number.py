def kaprekar(n):
    k = n**2
    for i in range(1,len(str(k))):
        if n == (k//10**i) + (k%10**i) and (k%10**i):
            return True
    return False

n = int(input())
print(kaprekar(n))