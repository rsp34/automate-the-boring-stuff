#! python3

import os
import glob
import shutil

def selectiveCopy(source,destination,myGlob):
    for root, dirs, files in os.walk(source):
            matched_files = glob.glob(os.path.join(root,myGlob))
            for matched_file in matched_files:
                source_path =  os.path.join(root,matched_file)
                destination_path = os.path.join(destination,os.path.basename(matched_file))
                if source_path is not destination_path:
                    try:
                        shutil.copy(source_path,destination_path)
                    except shutil.SameFileError:
                        print(f'{os.path.basename(matched_file)} already in {destination}')
                    except PermissionError:
                        print(f'Permission denied for {os.path.basename(matched_file)}')
selectiveCopy("C:\\Users\\Ryan\\Desktop","C:\\Users\\Ryan\\Desktop\my_pdfs","*.pdf")