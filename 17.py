n=int(input())
h=0
a=n
while a>0:
 digit =a%10
 h +=digit**3
 a //=10
if n==h:
 print("yes")
else:
 print("no")
  
