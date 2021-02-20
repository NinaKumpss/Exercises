# Write your code here
def from_lists(keys, values):
    #return dict(zip(keys, values))
    result = {k:v for k,v in zip(keys, values)}
    return result