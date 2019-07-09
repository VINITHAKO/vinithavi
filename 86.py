v1=list(input())
i=[]
for j in v1:
   if j not in i:
      i.append(j)
if v1==i:
   print("Yes")
else:
   print("No")
