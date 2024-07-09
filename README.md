# Book_Scraper
"""
This application was created and tested using the following system specifications
1. Windows 10
2. Python 3.12.4

Scraping is done by using BeautifulSoup4 and Requests which are included as part of the requirements text file.

This application uses multiple scripts called on by the main application script in order to do the following: 
1. Extract data from books.toscrape.com based on the URL provided
   a. This URL will determine whether a single category is scraped or all categories (if the main url is provided)
2. Transform the data into a csv readable format using lists and hard coding the delimiter as ';'
3. Load two sets of data: 
   a. Category CSVs to show all applicable data for a given book
   b. Cover pages for each book downloaded as .jpg files

In order to setup the application you will need to perform the following steps: 
1. Create a new folder in the C directory as follows: 
   a. C:\Open Classrooms Projects\Book_Scraping
2. Ensure Python (latest version) is installed
3. Open Command Prompt
4. Type Python and click enter
5. Type git clone https://github.com/dannyjf93/Book_Scraper.git and click enter
6. Type cd Book_Scraper and click enter
7. Type python -m venv env and click enter
8. Type env\Scripts\activate and click enter
9. Type pip install -r requirements.txt and click enter

Now that the application has been set up and the requirements have been installed you can view possible commands using the below prompt (type and click enter)
1. python main.py --help

If you would like to scrape all categories you can use the below prompt (type and click enter): 
1. python main.py

If you would like to only scrape a specific category you can use the below prompt (below is just an example. You can type any category name you would like)
(type and click enter): 
1. python main.py categories --travel
"""