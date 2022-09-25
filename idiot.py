import pyinputplus as pyip
while True:
    response = pyip.inputYesNo('Want to know how to keep a sweet puss busy for hours?\n')
    if response == 'no':
        break
print('Thank you. Have a nice day.')