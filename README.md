# Book_Scraper
###
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
1. Ensure Python (latest version) is installed
2. Open Windows PowerShell
3. Type git clone https://github.com/dannyjf93/Book_Scraper.git and click enter
4. Type cd Book_Scraper and click enter
5. Type python -m venv env <directory> and click enter #Copy and paste the newly created directory where <directory> is shown (usually C:\Users\Username\Book_Scraper)
6. Type Scripts\activate.ps1 and click enter
   a. If you run into an error related to running scripts being disabled you can bypass using the following command: 
      Set-ExecutionPolicy Unrestricted -Scope Process
   b. When prompted, type Y and click enter to allow scripts to be activated
7. Type pip install -r requirements.txt and click enter

Now that the application has been set up and the requirements have been installed you can run the application.

In order to run the application follow the below commands: 
1. Type python Scrape_Books.py and click enter
2. You will then be prompted to paste a URL to be scraped and you have two options: 
   a. If you would like to scrape all categories available, copy and paste the main https://books.toscrape.com/index.html URL
   b. If you would only like to scrape a single category, navigate to that category and copy/paste that URL into the prompt
3. The application will run once a valid URL is pasted and the user clicks enter
4. All exported data can be found in the newly created directory in which a newly created "Exported_Data" folder will be available. 
   a. Data is split up into a "Category_CSVs" folder for actual product information by category and a "Cover_Pages" folder for the book images input into their own category folders.
###

###
Future improvements to make: 
Create simple GUI for ease of use - allow for user to open GUI, click Run, paste input for prompt, and application will export data as expected
Update main application with cancel option if started but user wishes to cancel operation
###