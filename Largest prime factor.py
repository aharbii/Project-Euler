import sys
import math


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = 0
    while (n%2 == 0):
        p = 2
        n /= 2
    
    for i in range(3, int(math.sqrt(n))+1, 2):
        while (n%i == 0):
            p = i
            n /= i
    if (n > 2):
        p = n

    print(int(p))
