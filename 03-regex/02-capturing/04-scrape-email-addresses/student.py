# Write your code here
import re
def scrape_email_addresses(string):
    #\S == matches any non-whitespace character
    return re.findall('\S+@\S+', string)