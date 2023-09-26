import requests
from bs4 import BeautifulSoup
import time

url = "https://www.discudemy.com/all" # Define the URL to scrape

def scrape_first_url(url):
    response = requests.get(url)# Send an HTTP GET request to the specified URL
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        card_header_elements = soup.find_all(class_="card-header")
        href_links = []
        for links in card_header_elements:
            href = links.get('href')
            href_links.append(href)
        scrap_second(href_links)      

def scrap_second(links):
    for link in links:
        response = requests.get(link)
        soup = BeautifulSoup(response.text, 'html.parser')
        card_header_element = soup.find(class_="ui big inverted green button discBtn")
        if card_header_element:
            href = card_header_element.get('href')
            scrap_third(href)

def scrap_third(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text, 'html.parser')   
    card_header_elements = soup.find(id="couponLink")
    href = card_header_elements.get('href')
    print(href)

def main():
    scrape_first_url(url)

if __name__ == "__main__":
    main()
