d = {}

def search(pr, ch):
    return ch == pr or any(map(lambda pl: search(pr, pl), d[ch]))

for i in range(int(input())):
    s1 = input().split(':')
    if len(s1) == 1:
        d[s1[0].strip()] = []
    else:
        d[s1[0].strip()] = [x.strip() for x in s1[1].split()]

q, p = [], []
for i in range(int(input())):
    q.append(input())
i = 0
while i < len(q):
    j = 0
    for j in range(i):
        if search(q[j], q[i]) and q[i] not in p:
            p.append(q[i])
    i += 1
for i in p:
  print(i)