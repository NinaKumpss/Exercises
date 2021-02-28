# Write your code here
def is_increasing(ns):
    return (all(i <= j for i, j in zip(ns, ns[1:])))