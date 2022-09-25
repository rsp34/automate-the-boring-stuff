#! python3

from select import select
from urllib import request
import webbrowser, bs4, sys, requests

# Get command line arguments
if len(sys.argv)>1:
    search_terms = sys.argv[1:]
else:
    search_terms = ["numpy"]
#    raise ValueError('Input argument expected')

# Open PYPI
res = requests.get("https://pypi.org/search/?q="+" ".join(search_terms))
if res.ok:
    search_soup = bs4.BeautifulSoup(res.text,'html.parser')
else:
    raise ValueError('No response from site')

link_elems = search_soup.select('.package-snippet')
num_open = min(5, len(link_elems))
for i in range(num_open):
    webbrowser.open_new_tab("https://pypi.org/"+link_elems[i].get("href"))










