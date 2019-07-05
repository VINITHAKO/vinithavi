vi,de=map(int,input().split())
vi=vi*de
for i in range(0,vi+1):
 if(i**2==0):
  print("yes")
  break
else:
 print("no")
