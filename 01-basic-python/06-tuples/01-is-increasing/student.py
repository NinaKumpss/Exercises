# Write your code here
def is_increasing(ns):
    res = all(i <= j for i, j in zip(ns, ns[1:]))
    if res:
        return True
    else:
        return False