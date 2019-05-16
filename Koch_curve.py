a = []
def koch_turn(n):
    if n == 0: return
    else: 
      a.append(koch_turn(n-1))
      a.append(60)
      a.append(koch_turn(n-1))
      a.append(-120)
      a.append(koch_turn(n-1))
      a.append(60)
      a.append(koch_turn(n-1))

n = int(input())
koch_turn(n)
for i in a:
  if i is not None:
    print("turn", i)