import string
import sys
import time

import requests
from bs4 import BeautifulSoup as BS


def check_cmd_line():
    if len(sys.argv) != 2:
        print('Usage: script zipcode')
        sys.exit(1)
    if len(sys.argv[1]) != 5:
        print('Invalid Zipcode')
        sys.exit(1)


def urlscrape(url):
    page = requests.get(url)
    soup = BS(page.text, 'html.parser')

    return soup


def city(soup):
    city = soup.title.text.split(',')[0]
    return city.rstrip(string.punctuation + string.whitespace)


def population(soup):
    try:
        pop = soup.find(string="Total population").next_element.text
    except AttributeError:
        print('Invalid Zipcode')
        sys.exit(1)
    return pop.rstrip(pop[-1])


def print_data(city, population):
    print('\nTown Name:', city)
    print('Population:', population)


check_cmd_line()
url = f'https://www.uszip.com/zip/{sys.argv[1]}'
soup = urlscrape(url)
print_data(city(soup), population(soup))