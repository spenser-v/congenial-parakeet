#at least 8 characters long
#must have at least 1 uppercase and 1 lowercase letter
#must have at least 1 number
#feels better to do the password checks *after* the regex that finds pw...

#ADVANCED ANSWER:
#pw_regex = (?=[^\d\n]*\d)(?=[^A-Z\n]*[A-Z])(?=[^a-z\n]*[a-z])^[A-Za-z0-9]{8,}
import re

def strongPassword(password):
    if passRegex1.search(password) == None:
        return False
    if passRegex2.search(password) == None:
        return False
    if passRegex3.search(password) == None:
        return False
    if passRegex4.search(password) == None:
        return False
    else:
        return True

passRegex1 = re.compile(r'\w{8,}')
passRegex2 = re.compile(r'\d+')
passRegex3 = re.compile(r'[a-z]')
passRegex4 = re.compile(r'[A-Z]')
print('Input password.')
password = input()
if strongPassword(password) == True:
    print("Strong Password")
else:
    print("This is not a strong password")