v,i=map(int,input().split())
for k in range (v+1,i+1):
  if(k>1):
    for l in range (2,k):
      if(k%l==0):
        break
    else:
      print(k,end=" ")
