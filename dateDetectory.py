import re

def dateDetector(date):
    
    # Detect groups in the string
    dateRegex = re.compile('(\d\d)/(\d\d)/(\d\d\d\d)')
    
    # Convert strings to numeric values
    d = int(dateRegex.search(date).group(1))
    m = int(dateRegex.search(date).group(2))
    y = int(dateRegex.search(date).group(3))

    # Check if the dates are valid otherwise return none
    if d<1 and d>31:
        return None
    elif m<1 and m>12:
        return None
    elif y<1000 and y>2999:
        return None
    elif m in [9,4,6,11] and d==31:
        return None
    elif m==2 and not ((y%4==0 and y%100!=0) or y%400==0) and d>28:
        return None
    elif m==2 and ((y%4==0 and y%100!=0) or y%400==0) and d>29:
        return None

    return d,m,y

dateDetector('29/02/1500')