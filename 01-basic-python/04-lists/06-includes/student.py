# Write your code here
def includes(xs, ys):
    result = all(elem in xs for elem in ys)
    if result:
        return True
    else:
        return False

#    for y in ys:
#        if y not in xs:
#            return False
#    return True