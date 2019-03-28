import datetime

k = [int(i) for i in input().split()]
d1 = datetime.date(k[0], k[1], k[2])
delta = datetime.timedelta(int(input()))
d2 = d1 + delta
print(d2.strftime("%Y %m %d"))