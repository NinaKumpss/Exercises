# Write your code here
def word_count(string):
    #removing spaces from start to end
    zin = string.strip()
    count = 1
    for i in zin:
        #als er een spatie is, count +1 doen
        if i == " ":
            count += 1
    return count