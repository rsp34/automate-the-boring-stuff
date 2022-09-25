import time, sys
indent = 0
maxIndent = 20
indentIncreasing = True
try:
    while True:
        # Infinite loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) 

        # Check whether we need to change whether indent is increasing or decreasing
        if indent == maxIndent:
            indentIncreasing = False
        elif indent == 0:
            indentIncreasing = True

        # Modify indent
        if indentIncreasing:
            indent += 1
        else:
            indent -= 1
except KeyboardInterrupt:
    sys.exit()
