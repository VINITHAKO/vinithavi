vin=input()
s=['a','A','e','E','i','I','o','O','u','U']
for i in vin:
 if i in s:
  print("yes")
  break
else:
 print("no")
