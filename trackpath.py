matrix=[['a', 'b', 'c', 'd', 'e', 'f'],
 ['e', 'g', 'h', 'i', 'j', 'k'],
 ['l', 'm', 'n', 'o', 'p', 'q'],
 ['r', 's', 't', 'u', 'v', 'w'],
 ['x', 'y', 'z', '1', '2', '3'],
 ['4', '5', '6', '7', '8', '9']]
# for i in range(6):
#   a=input().split()
#   matrix.append(a)
frm=input("enter start position: ")
to=input("enter end point: ")
aa=0
for i in matrix:
  for j in i:
    aa+=1
    if j==frm:
      frm=False
      break
  if frm==False:
    break
a=0
for i in matrix:
  for j in i:
    a+=1
    if j==to:
      to=False
      break
  if to==False:
    break
a=a-aa
q=int(a/6)
if(a<0):
  r=-1*((-1*a)%6)
else:
  r=a%6
if r>0:
  for i in range(r):
    print("move right")
elif r<0:
   for i in range(r*-1):
    print("move left")
if q>0:
  for i in range(q):
    print("move down")
elif q<0:
  for i in range(q*-1):
    print("move up")
