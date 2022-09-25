#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil, os, re
from pathlib import Path

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
                        ((0|1)?\d)-                     # one or two digits for the month
                        ((0|1|2|3)?\d)-                 # one or two digits for the day
                        ((19|20)\d\d)                   # four digits for the year
                        (.*?)$                          # all text after the date
                        """, re.VERBOSE)

# TODO: Loop over the files in the working directory.
cwd = Path.cwd()
for files in os.listdir(Path.cwd()):
    mo = datePattern.search(files)
    if mo:
        text_before_date = mo.group(1)
        month = mo.group(2)
        day = mo.group(4)
        year = mo.group(6)
        text_after_date = mo.group(8)

        new_name = f'{text_before_date}{day}-{month}-{year}{text_after_date}'

        old_path = cwd / files
        new_path = cwd / new_name

        shutil.move(old_path,new_path)
        print(f'Renaming "{old_path}" to "{new_path}"...')