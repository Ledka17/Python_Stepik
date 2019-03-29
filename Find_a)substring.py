s, s1 = input(), input()
if s.find(s1) == -1:
    print('-1')
else:
    for i in range(len(s)-len(s1)+1):
        if s[i:i+len(s1)] == s1:
          print(i, end=' ')