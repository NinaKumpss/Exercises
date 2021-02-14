# Write your code here
def format_time(h, m, s):
    #result = str(h) + ":" + str(m) + ":" + str(s)
    result = str(h).rjust(2,"0") + ":" + str(m).rjust(2,"0") + ":" + str(s).rjust(2,"0")
    #result = f'{h}:{m}:{s}'
    return result