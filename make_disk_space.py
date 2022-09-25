#! python3

import pandas as pd, os
from tabulate import tabulate

def make_disk_space(source: str, nFiles: int=5):
    dict_list = []
    for root, dirs, files in os.walk(source):
        for file in files:
            fullpath = os.path.join(root,file)
            size = os.path.getsize(fullpath)
            dict_list.append({"path":fullpath,"size":size})
    
    df = pd.DataFrame(dict_list)
    df = df.sort_values(by=['size'],ascending=False).iloc[0:nFiles]
    print(tabulate(df, headers='keys', tablefmt='psql',showindex=False))

make_disk_space("C:\\Users\\Ryan\\Desktop")