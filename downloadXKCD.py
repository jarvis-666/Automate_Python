import os
import requests
import bs4

def main():
    base_url = "http://xkcd.com"
    os.makedirs(r"./xkcd", exist_ok=True)
    n = int(input("How many images do you want?: "))
    while not base_url.endswith('#') and n > 0:
        print("Downloading page", base_url)
        res = requests.get(base_url)
        res.raise_for_status()
        comicSoup = bs4.BeautifulSoup(res.text)
        comicElem = comicSoup.select('#comic img')
        if comicElem == []:
            print("Could not find comic image")
        else:
            comicURL = 'http:' + comicElem[0].get('src')
            print("Image Found. Downloading image", comicURL)
            res = requests.get(comicURL)
            res.raise_for_status()
            imageFile = open(os.path.join('./xkcd', os.path.basename(comicURL)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        prevLink = comicSoup.select('a[rel="prev"]')[0]
        base_url = 'http://xkcd.com' + prevLink.get('href')
        n -= 1
    print('Done')

if __name__ == "__main__":
    main()