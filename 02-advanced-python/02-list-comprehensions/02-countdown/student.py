# Write your code here
def countdown(n):
    result = ""
    while n > 0:
        result += str(n)
        n -= 1
    return (", ".join(result))