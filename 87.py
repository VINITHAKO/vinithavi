d3,d4=map(int,input().split())
v=1
while(v<=d3 and v<=d4):
 if(d3%v==0 and d4%v==0):
  gcd=v
 v=v+1
print(gcd)
