delta = int(input())
s1 = input()
s2 = ''
dic = ' abcdefghijklmnopqrstuvwxyz'
for i in range(len(s1)):
    s2 += dic[(dic.find(s1[i]) + delta) % 27]
print('Result: "'+s2+'"')
