#import libraries
import time
import requests
from bs4 import BeautifulSoup
from category_iteration import get_category_pages_urls

def main():
    #Prompt the user to choose whether they want to scrape the entire website or only one category
    print("\n Scraping books.toscrape.com\n")
    time.sleep(1)
    main_url = 'https://books.toscrape.com/'
    response = requests.get(main_url)

    #If response is successful prompt user to paste URL for entire website or url for one category
    if response.status_code == 200:
        print("\n- connection ok -")
        soup = BeautifulSoup(response.text, 'html.parser')
        category_url_list = [main_url + line["href"] for line in soup.select("ul > li > ul > li > a")]

        url = input('\n\nPaste the url you would like to scrape: ')
        start_time = int(time.time())

        if url.replace('index.html', '') == main_url:
            print("\nExporting all categories...\n")
            for i in range(len(category_url_list)):
                get_category_pages_urls(category_url_list[i])
            timer(start_time)
            time.sleep(1)
            print('\n------END------')

        elif url in category_url_list:
            index = category_url_list.index(url)
            category_url = category_url_list[index]
            get_category_pages_urls(category_url)
            timer(start_time)
            time.sleep(1)
            print('\n------END------')

        else:
            print('\n\nPlease enter a valid url (full website or one category).\n\n')
            time.sleep(2)
            main()
    #retry if error bad response received - if bad response is continuous application will close
    else:
        response.raise_for_status()
        print("\n- connection error -")
        print("Please check connection status.")
        time.sleep(1)
        retry = input("Retry? (y/n) :").lower().strip()
        while retry != "y" != "n":
            print("input error")
            retry = input("Retry? (y/n) :").lower().strip()
        if retry == "y":
            print("Restarting")
            time.sleep(2)
            main()
        elif retry == "n":
            print('Closing application')
            time.sleep(2)
            exit()


def timer(start_time):
    end_time = int(time.time()) - start_time
    mins = end_time // 60
    secs = end_time % 60
    end_time = '{:02d} mins {:02d} secs.'.format(mins, secs)
    print('\n\nAll books exported in ' + end_time)


if __name__ == "__main__":
    main()