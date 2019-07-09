vo=int(input())
vi=list(map(int,input().split()))
for i in range(len(vi)-1):
 if(vi[i]>vi[i+1]):
  print(i)
