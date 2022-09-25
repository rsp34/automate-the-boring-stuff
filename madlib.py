from pathlib import Path
import pyinputplus as pyip
import re

mad_lib_path = Path("madlib.txt")
mad_lib_file = open(mad_lib_path)
mad_lib_text = mad_lib_file.read()
mad_lib_file.close()

word_regex = re.compile(r"ADJECTIVE|NOUN|ADVERB|VERB", re.IGNORECASE)
matches = word_regex.findall(mad_lib_text)

for match in matches:
    if match.lower() == "adjective":
        response = pyip.inputStr("Enter an adjective: ")
    elif match.lower() == "noun":
        response = pyip.inputStr("Enter a noun: ")
    elif match.lower() == "adverb":
        response = pyip.inputStr("Enter an adverb: ")
    elif match.lower() == "verb":
        response = pyip.inputStr("Enter a verb: ")
    mad_lib_text = mad_lib_text.replace(match, response, 1)

new_mad_lib_path = mad_lib_path.parent / (
    mad_lib_path.stem + "_new" + mad_lib_path.suffix
)
new_mad_lib_file = open(new_mad_lib_path, "w")
new_mad_lib_file.write(mad_lib_text)
new_mad_lib_file.close()
