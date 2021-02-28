# Write your code here
def divisors(n):
   # return [ k for k in range(1, n + 1) if n % k == 0 ]
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

    #for x in range(1, n+1):
    #    if(n % x ==0):
    #      return x  