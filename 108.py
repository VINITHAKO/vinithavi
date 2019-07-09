vv,kk=map(int,input().split())
ss=list(map(int,input().split()))
uu=[]
for i in ss:
 if(i<=i+1):
  uu.append(i)
print(uu[kk-1])
