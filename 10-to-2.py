def translate(i,n=2):
    s=''
    while i>=n:
        s = str(i%n) + s
        i //= n
    s = str(i) + s
    return int(s)

print(translate(10,8))
print(translate(10,7))
print(translate(4,2))