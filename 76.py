vi=int(input())
if(vi>1):
 for i in range(2,vi):
  if(vi%i==0):
   print("yes")
   break
 else:
  print("no")
