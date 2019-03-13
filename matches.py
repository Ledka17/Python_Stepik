s = input()
l,k = [], []
d = {'(':')', '[':']', '{':'}'}
for i in range(len(s)):
#    print('i=', i)
    if s[i] in ('(', '[', '{'):
        l.append(s[i]); k.append(i+1)
    else:
        if len(l) and d[l[len(l)-1]] == s[i]:
            l.pop(); k.pop()
        else:
            break
print('Success' if not len(k) and not len(l) else k.pop())