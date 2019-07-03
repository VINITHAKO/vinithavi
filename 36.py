d=input()
n=0
for i in range(len(d)):
 if(d[i].isdigit() or d[i].isalpha() or d[i]==(" ")):
  continue
 else:
  n+=1
print(n)
