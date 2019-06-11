import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    F = [2,8]
    i = 1
    while(F[-1] < n):
        F.append(4*(F[i])+F[i-1])
        i += 1
    F.pop()
    print(sum(F))
