# Write your code here
def is_prime(n):
    #return n > 1 and all( [ n % k != 0 for k in range(2, n) ] )

    if n < 2:
        return False
    elif n == 2:
        return True  
    for x in range(2, n):
        if n % x ==0:
            return False
    return True