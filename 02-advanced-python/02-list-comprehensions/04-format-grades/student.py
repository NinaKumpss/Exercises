# Write your code here
def format_grades(grades):
    avgDict = {}
    for k,v in grades.items():
    # v is the list of grades for student k
        avgDict[k] = round(sum(v)/ float(len(v)))

    res = '\n'.join(key + ": " + str(val) for key, val in avgDict.items()) 
    return res