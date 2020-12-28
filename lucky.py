import sys
import requests
import bs4
import re
import webbrowser

def get_from_CLI():
    print("We have a search query entered from CLI")
    query_to_search = ' '.join(sys.argv[1:])
    return query_to_search

def make_the_request(query_to_search):
    url_to_get = "http://google.com/search?q=" + query_to_search.replace(' ', '%20')
    print(url_to_get)
    res = requests.get(url_to_get)
    return res

def retrieve_urls(search_results, n):
    searchSoup = bs4.BeautifulSoup(search_results, 'html.parser')
    links = list(searchSoup.select('div > a[href]'))
    return links

def open_those_urls(links, n):
    useful_links = [a.get('href') for a in links]
    # print(useful_links)
    final = list()
    url_finder = re.compile(r"\?q=(https://[\S]+)")
    for i in useful_links:
        m = url_finder.findall(i)
        if m != []:
            final.append(m[0])
    # print(final)
    for i in final[:n]:
        if '&' in i:
            webbrowser.open(i.split('&')[0])
        else:
            webbrowser.open(i)

def main():
    print("Welcome to Google I'm Feeling Lucky Tool")
    query = get_from_CLI()
    print("The query to be searched is:", query)
    print("Thanks for feeding the query... Will fetch results now")
    search_results = make_the_request(query)
    print("Woohooo... We have the results... Processing them now")
    n = int(input("How many tabs do you want to open?: "))
    links = list()
    try:
        links = retrieve_urls(search_results.text, n)
    except:
        print("Please Wait")
    finally:
        print(f"We got {len(links)} links, opening {n} most relevant tabs for you now")
    open_those_urls(links, n)


if __name__ == "__main__":
    main()