import re

def strongPasswordDetector(password):

    """Write a function that uses regular expressions to make sure the password string it is passed is strong. A strong password is defined as one that is at least eight characters long, contains both uppercase and lowercase characters, and has at least one digit. You may need to test the string against multiple regex patterns to validate its strength."""

    eightCharacterRegex=re.compile('\S{8,}')
    upperCaseRegex=re.compile('[A-Z]{1,}')
    lowerCaseRegex=re.compile('[a-z]{1,}')
    digitRegex=re.compile('\d{1,}')

    if bool(eightCharacterRegex.search(password)) and bool(upperCaseRegex.search(password)) and bool(lowerCaseRegex.search(password)) and bool(digitRegex.search(password)):
        return 'Strong'
    else:
        return 'Weak'

print(strongPasswordDetector('Abhelllllooo1'))