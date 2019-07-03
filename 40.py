v=int(input())
g1,g2=0,1
print(g2,end=" ")
for i in range(1,v):
 g3=g1+g2
 print(g3,end=" ")
 g1,g2=g2,g3
