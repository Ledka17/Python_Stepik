s,t = input(), input()
k = len(t)
n = 0
for i in range(0, len(s)-k+1):
    if s[i:i+k] == t:
        n += 1
print(n)