def isin(s1):
  for i in range(1, len(s1)+1):
    if i not in s1:
      print("Not jolly")
      return
  print("Jolly")
  return

s = input().split()
if len(s) == 1:
  print("Jolly")
else:
  s1 = [abs(int(s[i]) - int(s[i+1])) for i in range(len(s)-1)]
  isin(s1)