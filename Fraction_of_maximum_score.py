a = [i for i in input().split()]
sum = len(a)
sumA = 0
for i in a:
    if i == 'A': sumA+=1 
a = sumA/sum
print("%.2f" % a)