import sys
z=int(input())
if z%600==0 or (z%6==0 and z%100!=0):
    print('yes')
else:
    print('no')
