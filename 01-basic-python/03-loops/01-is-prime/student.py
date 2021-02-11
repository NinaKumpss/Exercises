# Write your code here
def is_prime(n):
    if n <= 1:
        return False
    else:
        for i in range(2,n):
            #checking for factor
            if n % i == 0:
                return False
    return True