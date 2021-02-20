# Write your code here
def remove_duplicates(xs):
    dubbel = set()
    #bij een list ==> dubbel = []
    result = []
    for x in xs:
        if x not in dubbel:
            result.append(x)
            dubbel.add(x)
    return result