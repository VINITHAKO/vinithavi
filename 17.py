t=int(input())
h=0
a=t
while a>0:
 digit =a%10
 h +=digit**3
 a //=10
if t==h:
 print("yes")
else:
print("no")
  
