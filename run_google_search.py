import requests
from bs4 import BeautifulSoup


def search(question : str) -> str:
    res = requests.get('https://www.google.com/search?q=' + question)
    return res.content

def main(): 
    question = input()
    html = search(question)
    print(html)

if __name__ == '__main__':
    main()
