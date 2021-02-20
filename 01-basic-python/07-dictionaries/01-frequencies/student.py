# Write your code here
def frequencies(xs):
    aantal = {}

    for x in xs:
        aantal[x] = aantal.get(x, 0) + 1
    return aantal