def punctuateList(l):
    punctuatedList = ''
    nItems = len(l)
    for i in range(nItems):
        punctuatedList += l[i]
        if i == nItems-2:
            punctuatedList += ' and '
        elif i<nItems-2:
            punctuatedList += ', '
    return punctuatedList

myList = ['apple','orange','sheep','mouse']
print(punctuateList(myList))