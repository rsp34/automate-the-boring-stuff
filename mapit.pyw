#! python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.

import pyperclip, sys, webbrowser

# Get address from pyperclip or command line arguments
if len(sys.argv) == 1:
    address = pyperclip.paste()
else:
    address = " ".join(sys.argv[1:])

# Generate a query string
webbrowser.open("https://www.google.co.uk/maps/place/" + "+".join(address.replace(",", " ").split()))