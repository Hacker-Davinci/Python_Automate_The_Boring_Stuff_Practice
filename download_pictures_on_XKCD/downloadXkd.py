#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
#todo you need to spend time to understand .get doing  in requests
import requests, os, bs4

url = 'http://xkcd.com'     #starting url
os.makedirs("xkcd", exist_ok=True) # store comics in ./xlcd
while not url.endswith('#'):
    # TODO: Download the page.
    print("Downlaoding page %s..." % url)
    res = requests.get(url)
    res.raise_for_status() # to check whether get correctly.

    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: Find the URL of the comic image.
    comicElem = soup.select("#comic img")
    if comicElem == []:
        print("Could not find comic image.")
    else:
        comicUrl = "http:" + comicElem[0].get('src')
        # TODO: Download the image.
        print("Downloading image %s..." % (comicUrl))
        res = requests.get(comicUrl)
        res.raise_for_status()
        # TODO: Save the image to ./xkcd
        imageFile = open(os.path.join("xkcd", os.path.basename(comicUrl)), 'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

    # TODO: Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = "http://xkcd.com" + prevLink.get("href")

print("Done.")






