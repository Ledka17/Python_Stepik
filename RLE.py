def rle (a): #rle сжатие
  s1 = ''
  k = 1
  a = a + '0'
  for i in range (len(a)-1):
    if a[i] == a[i+1]:
       k += 1
    else:
      if k != 1:
        s1 += str(k)
        k = 1
      s1 += a[i]
  return len(s1)

def rleo(s): #распаковка кд
  s1 = ''
  i = 0
  while i < len(s):
    k = 0
    while s[i+k] >= '0' and s[i+k] <= '9':
      k += 1
    if k != 0:
      n = int(s[i:i+k])
      for j in range(n-1):
        s1 += s[i+k]
    s1 += s[i+k]
    i += k+1
  return s1

s = input()
s1 = rleo(s)
res = []
n = int(input())
for i in range(n):
  ch = input()
  f = int(ch[:ch.find(" ")])
  l = int(ch[ch.find(" ") + 1:])
  res.append(str(rle(s1[f-1:l])))
for i in range(n):
  print(res[i])