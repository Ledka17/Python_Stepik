d = {}

def search(pr, ch):
    return ch == pr or any(map(lambda pl: search(pr, pl), d[ch]))

for i in range(int(input())):
    s1 = input().split(':')
    if len(s1) == 1:
        d[s1[0].strip()] = []
    else:
        d[s1[0].strip()] = [x.strip() for x in s1[1].split()]

q = []
for i in range(int(input())):
    q.append(input().split())
for q1 in q:
    if search(q1[0], q1[1]):
        print('Yes')
    else:
        print('No')