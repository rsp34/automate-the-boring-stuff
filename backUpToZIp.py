#! python3
# backupToZip.py - Copies an entire folder and its contents into
# # a ZIP file whose filename increments.

import zipfile, os

def backupToZip(folder):
    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)   # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # TODO: Create the ZIP file
    print(f'Creating {zipFilename}...')
    with zipfile.ZipFile(zipFilename, 'w') as zip:
        for foldername, subfolders, filenames in os.walk(folder):
            print(f'Adding files in {foldername}...')
            zip.write(foldername)
            for filename in filenames:
                newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files
            zip.write(os.path.join(foldername, filename))
            zip.close()



    # TODO: Walk the entire folder tree and compress the files in each folder.
    print('Done.')

backupToZip('C:\\delicious')