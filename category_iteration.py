#import libraries
import re
import requests
from bs4 import BeautifulSoup
from get_book_data import extract_book_info
from create_csv import create_csv_file

#Get category name from category url string
def get_category_name(category_url):
    category_name = category_url.replace('https://books.toscrape.com/catalogue/category/books/', '')
    category_name = category_name.replace('/index.html', '').replace('_', '').replace('-', ' ')
    category_name = re.sub(r'[0-9]+', '', category_name)

    print("\nExporting " + category_name.title() + "\n")
    return category_name

#Get total number of books in current category
def get_category_pages_urls(category_url):
    category_name = get_category_name(category_url)
    response = requests.get(category_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    books_total = int(soup.select_one("form > strong").text)
    if books_total > 20:
        page_total = int(soup.find("li", {"class": "current"}).text.replace("Page 1 of", ""))
    else:
        page_total = 1

    csv_filename = category_name.lower().replace(' ', '_') + ".csv"
    create_csv_file(csv_filename)

    page_url = category_url
    current_category_pages = [page_url]
    #iterate through each page of the category
    for page in range(page_total):
        if page == 0:
            book_url_list = extract_book_urls(current_category_pages[0])
            for x in range(len(book_url_list)):
                extract_book_info(book_url_list[x], category_name, csv_filename)
        else:
            current_category_pages.append(page_url.replace("index", "page-" + str(page + 1)))
            book_url_list = extract_book_urls(current_category_pages[page])
            for x in range(len(book_url_list)):
                extract_book_info(book_url_list[x], category_name, csv_filename)

#For each page, add cleaned book url to a list
def extract_book_urls(category_page):
    response = requests.get(category_page)
    soup = BeautifulSoup(response.text, 'html.parser')
    book_url_list = []
    book_url = [line["href"] for line in soup.select("ol > li > article > h3 > a")]
    for book in range(len(book_url)):
        book_url_clean = book_url[book].replace("../../../", "https://books.toscrape.com/catalogue/")
        book_url_list.append(book_url_clean)

    return book_url_list