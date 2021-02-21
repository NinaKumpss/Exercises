# Write your code here
def nth_longest_string(n, strings):
    ordered = sorted(strings, key = len)
    return ordered[-n]