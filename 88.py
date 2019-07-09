v1,d1=map(int,input().split())
maxima=max(v1,d1)
while(1):
 if(maxima%v1==0 and maxima%d1==0):
  print(maxima)
  break
 maxima+=1
