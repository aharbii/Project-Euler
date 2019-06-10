import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    def preSum(q):
        return (q*(1+q) //2 )
    result = 3*preSum(int((n-1)//3)) + 5*preSum(int((n-1)//5)) - 15*preSum(int((n-1)//15))
    print(int(result))
