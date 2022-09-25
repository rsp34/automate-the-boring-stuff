import re

def isPhoneNumber(text):
    if len(text) != 12:
        # Must be 12 characters
        return False
    for i in range(0, 3):
        # First 3 are numbers
        if not text[i].isdecimal():
            return False
    if text[3] != "-":
        # Then a hyphen
        return False
    for i in range(4, 7):
        # Another 3 numbers
        if not text[i].isdecimal():
            return False
    if text[7] != "-":
        # Another hyphen
        return False
    for i in range(8, 12):
        # The remainder are digits
        if not text[i].isdecimal():
            return False
    return True

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

print("Is 415-555-4242 a phone number?")
print(isPhoneNumber("415-555-4242"))
print("Is Moshi moshi a phone number?")
print(isPhoneNumber("Moshi moshi"))
