s = input()
i = 0
while i<len(s):
    j = 0
    if s[i]>= '0' and s[i]<='9':
        while s[i+j]>= '0' and s[i+j]<='9':
            j += 1
        for k in range(int(s[i:i+j])):
            print(s[i+j], end='')
        i += j + 1
    else:
        print(s[i], end='')
        i += 1