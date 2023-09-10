import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def search(question : str) -> str:

    # run google search
    page = requests.get('https://www.google.com/search?q=' + question)

    # get the response from google and find the first relevant result
    # get the URL from that
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all('a')
    for link in links:
        url = link['href']
        if url.startswith('/url?q='):
            parsed_url = urlparse(url)
            params = parse_qs(parsed_url.query)
            #print(url)
            #print(params['q'][0])
            return params['q'][0]
    
    # Really?  can't find anything
    return None

def get_more_details(url : str) -> str:
    
    # Go to the web page returned from Google search
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html5lib")

    # Get all the content and print 
    result = ''
    paragraphs = soup.find_all('p')
    if paragraphs:
        for paragraph in paragraphs:
            result += " ".join(paragraph.get_text().split())
            result += '\n\n'
                
    # return the result
    return result

def main(): 
    question = 'How can poop determine how healthy a patient is'
    url = search(question)
    result = get_more_details(url)
    print(question + '?')

    print('\n\nAccording to ' + url)
    print ('=' * 90)
    print (result)


if __name__ == '__main__':
    main()