t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p = [2,3,5,7,11,13,17,19,23,29,31,37]
    x = 1
    for i in p:
        if i <= n:
            for j in range(1,6):
                if(i**j <= n):
                    x *= i
    print (x)
