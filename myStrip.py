import re

def myStrip(input,*args):

    """Write a function that takes a string and does the same thing as the strip() string method. If no other arguments are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of the string. Otherwise, the characters specified in the second argument to the function will be removed from the string."""

    if args:
        replaceRegex = re.compile(replace)
        return replaceRegex.sub('',input)
    else: 
        replaceRegex1 = re.compile('^\s*')
        replaceRegex2 = re.compile('\s*$')
        return replaceRegex2.sub('',replaceRegex1.sub('',input))

print(myStrip('      test        es      ')+'.')