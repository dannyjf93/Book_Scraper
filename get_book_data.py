#import libraries to be used
import re
import requests
from bs4 import BeautifulSoup
from create_csv import csv_file_append, download_images

#Get book info and add to a list
def extract_book_info(book_url, category_name, csv_filename):
    response = requests.get(book_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_info = soup.find_all('td')
    upc = product_info[0].text
    price_including_tax = product_info[3].text
    price_excluding_tax = product_info[2].text
    availability = product_info[5].text
    quantity_available = re.sub('[^0-9]', '', availability)
    title = str(soup.find('h1').text)
    description = soup.select_one('article > p').text.replace(' ...more', '')
    if description.isspace():
        description = 'N/A'

    review_rating = get_review_rating(soup.select_one('.star-rating').attrs['class'][1])
    image = soup.find('div', {'class': 'item active'}).find('img')
    image_url = image['src'].replace('../../', 'https://books.toscrape.com/')
    #improvement: create dataframe using pandas for below list
    info = [book_url,
            upc,
            title,
            price_including_tax,
            price_excluding_tax,
            quantity_available,
            description,
            category_name,
            str(review_rating) + ' star(s)',
            image_url
            ]

    csv_file_append(csv_filename, info)
    download_images(title, upc, image_url, category_name)

#compare star rating string to possible ratings list elements and convert to integer
def get_review_rating(rating):
    ratings = ['One', 'Two', 'Three', 'Four', 'Five']
    for i, mark in enumerate(ratings):
        if rating == mark:
            return i + 1