n,i=map(int,input().split())

for j in range(n+1,i):
  fin=j
  fd=0
  while (j>0):
    dt=j%10
    fd=fd+(dt**3)
    j=j//10
    if(fd==fin):
      print(fd,end=" ")
