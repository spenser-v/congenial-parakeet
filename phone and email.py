#! python3
#phone and email.py - finds phone numbers and email addresses in clipboard text

#accept text input
#find phone numbers
#find email addresses
#save to new document


import pyperclip, re

#PHONE NUMBER REGEX
phone_number_regex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

#EMAIL
email_regex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   # username
@                   # @ symbol
[a-zA-Z0-9.-]+      # domain name
(\.[a-zA-Z]{2,4})   # dot-something
)''', re.VERBOSE)

#LOAD INPUT TEXT
text = str(pyperclip.paste())

#FIND MATCHES IN INPUT TEXT
matches = []
for groups in phone_regex.findall(text):
    phone_number = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_number += ' x' + groups[8]
    matches.append(phone_number)
for groups in email_regex.findall(text):
    matches.append(groups[0])

#COPY RESULTS TO CLIPBOARD
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')