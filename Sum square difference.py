import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    a = (n*(n+1) //2) **2
    b = (n*(n+1)*(2*n+1) // 6) 
    print (a-b)
