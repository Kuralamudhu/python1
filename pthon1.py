import sys
a,b,c=map(int,(input('enter 3 no').split()))
if a>b and a>c:
  print(a)
elif b>c:
  print(b)
else:
  print(c)
