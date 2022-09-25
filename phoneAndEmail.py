#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
    )''', re.VERBOSE)


# Allowed characters: letters (a-z), numbers, underscores, periods, and dashes.
# An underscore, period, or dash must be followed by one or more letter or number.
# Allowed characters: letters, numbers, dashes.
# The last portion of the domain must be at least two characters, for example: .com, .org, .cc

emailRegex = re.compile(r'''(
    ([\w\d]+[_.-])*   # Optionally match one or more alphanumeric characters followed  .,-._
    ([\w\d]+)         # Alphanumeric before @ 
    (@)               # @
    ([\w\d]+[_.-])*   # optionally allow for more complex domain names
    ([\w\d]+)         # domain name
    (\.[\w\d]{2,})    # top-level domain
    )''', re.VERBOSE)

# Find matches in clipboard text.
txt = pyperclip.paste()
matches = []
for groups in phoneRegex.findall(txt):
       phoneNum = '-'.join([groups[1], groups[3], groups[5]])
       if groups[8] != '':
           phoneNum += ' x' + groups[8]
       matches.append(phoneNum)

for groups in emailRegex.findall(txt):
       matches.append(groups[0])

# Copy results to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')

## Create email regex.
#emailRegex = re.compile(r'''(
#    [a-zA-Z0-9._%+-]+      # username
#    @                      # @ symbol
#    [a-zA-Z0-9.-]+         # domain name
#    (\.[a-zA-Z]{2,4})      # dot-something
#    )''', re.VERBOS