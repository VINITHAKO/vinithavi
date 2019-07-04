g2,d2=map(int,input().split())
n3=list(map(int,input().split()[:g2]))
count=0
for i in n3:
   if(i==d2):
      count=count+1
print(count) 
