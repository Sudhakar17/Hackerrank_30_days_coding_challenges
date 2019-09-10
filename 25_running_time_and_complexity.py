import math
t = int(input())

def prime_checker(n):
    prime_flag = True
    sqrt_n = int(math.sqrt(n))
    for i in range(2, (sqrt_n+1)):
        if (n % i) == 0:
            prime_flag = False
            return prime_flag
    return prime_flag



for i in range(t):  
    n = int(input())
    if n > 1:
        prime_flag = prime_checker(n)
        if prime_flag:
            print("Prime")
        else:
            print("Not prime")
    else:
        print("Not prime")

