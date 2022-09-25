import requests, bs4
from PIL import Image
from io import BytesIO
from pathlib import Path

# Create output folder
output_path = Path(r'C:\Users\Ryan\xkcd')
next_page = "https://xkcd.com"
last_page = ""
while next_page is not last_page:
    res = requests.get(next_page)
    if res.ok:
            search_soup = bs4.BeautifulSoup(res.text,'html.parser')
    else:
        raise ValueError('No response from site')

    # Get image
    link_elems = search_soup.select('#comic > img:nth-child(1)')
    if link_elems==[]:
        continue
    img_url = link_elems[0].get("src")

    r = requests.get("https:"+link_elems[0].get("src"))
    i = Image.open(BytesIO(r.content))
    i.save(output_path/Path(img_url).name)

    # Get next page
    last_page = next_page
    prev_link  = search_soup.select("ul.comicNav:nth-child(4) > li:nth-child(2) > a:nth-child(1)")[0]
    next_page = "https://xkcd.com"+prev_link.get("href")

