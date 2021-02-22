# Write your code here
def slug(name):
    splitsing = name.split(" ") 
    voornaam = splitsing[0]
    plakken = "-".join(splitsing[1:])
    if len(splitsing) == 1:
        return voornaam.lower()
    else:
        return plakken.lower() + "-" + voornaam.lower()