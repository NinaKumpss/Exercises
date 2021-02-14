# Write your code here
def median(ns):
    n = len(ns)
    index = n // 2
     # Sample with an odd number of observations
    if n % 2:
        return sorted(ns)[index]
     # Sample with an even number of observations
    return sum(sorted(ns)[index - 1:index + 1]) / 2


    #ns.sort()
    #midden = (len(ns) -1)/2
    #if len(ns) // 2 != 0:
    #    return midden/2
    #else:
    #    return midden
