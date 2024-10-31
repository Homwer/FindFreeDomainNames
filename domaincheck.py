# Just a few lines of code that goes through possible domain names and checks the whois status.
# If the status is not set, the domain might be avaliable written to a file.
# Used it to check unknown endings.
#
# Requrements: 
# pip install whoisdomain

import string
import whoisdomain as whois

ending = ".ax"
a=list(string.ascii_lowercase)
b=list(string.ascii_lowercase)

file = open('domains.txt','w')

for x in a:
        for y in b:
                domain = x+y+ending
                d_check = whois.query(domain)
                if not hasattr(d_check, 'status'):
                        print ("Domain unregistered: " + domain)
                        file.write(domain+'\n')

print ("Done")
file.close()
