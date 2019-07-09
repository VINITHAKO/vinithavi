v,de=map(int,input().split())
ko=input().split()
e=[]
for i in ko:
 if(int(i)%2!=0):
  e.append(i)
print(e[de-1])
