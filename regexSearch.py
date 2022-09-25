import pyinputplus as pyip
from pathlib import Path
from pprint import pprint
import re
import os

directory = pyip.inputFilepath("Enter the directory you would like to search: ")
search_regex = re.compile(pyip.inputFilepath("Enter an expression to search for: "))
contents = os.listdir(Path(directory))

file_list = []
for item in contents:
    if os.path.isfile(Path(directory)/item):
        file = open(Path(directory)/item)
        text = file.read()
        file.close()
        if search_regex.match(text):
            file_list += search_regex.findall(text)

pprint(file_list)