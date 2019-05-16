d = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
ch = input()
sum = 0
for i in range(len(ch)-1):
    if d[ch[i]] < d[ch[i+1]]:
        sum -= d[ch[i]]
    else:
        sum += d[ch[i]]
sum += d[ch[i+1]]
print(str(sum))