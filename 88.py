e1,k1=map(int,input().split())
maxima=max(e1,k1)
while(1):
 if(maxima%e1==0 and maxima%k1==0):
  print(maxima)
  break
 maxima+=1
