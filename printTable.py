def printTable(t):
    colWidths = [0] * len(t)
    for iCol in range(len(colWidths)):
        for entry in t[iCol]:
            entryWidth = len(entry)
            if len(entry) > colWidths[iCol]:
                colWidths[iCol] = len(entry)

    for iRow in range(len(t[1])):
        print("\n", end="")
        for iCol in range(len(colWidths)):
            print(t[iCol][iRow].rjust(colWidths[iCol]), end="|")
    print("\n")


tableData = [
    ["apples", "oranges", "cherries", "banana"],
    ["Alice", "Bob", "Carol", "David"],
    ["dogs", "cats", "moose", "goose"],
]
printTable(tableData)
