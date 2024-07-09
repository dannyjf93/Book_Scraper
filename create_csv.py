#import libraries needed
import os
import csv
import requests

#Create directory
export_directory = 'Exported_Data'
#New venv would need to paste the appropriate parent directory below:
parent_directory = 'C:/Open Classrooms Projects/Book_Scraping/Book_Scraper'
path = os.path.join(parent_directory, export_directory)
if not os.path.isdir(path):
    os.mkdir(path)


#Create Exported_Data folder as well as .csv file within new folder
def create_csv_file(csv_filename):
    csv_directory = './Exported_Data/Category_CSVs'
    if not os.path.isdir(csv_directory):
        os.mkdir(csv_directory)
    with open('./Exported_Data/Category_CSVs/' + csv_filename, 'w', newline='', encoding='utf-8') as csv_file:
        book_csv = csv.writer(csv_file, delimiter=';')
        book_csv.writerow([
            'product_page_url',
            'UPC',
            'title',
            'price_including_tax',
            'price_excluding_tax',
            'number_available',
            'product_description',
            'category',
            'review-rating',
            'image_url'
        ])

#append extracted book information to csv file
def csv_file_append(csv_filename, info):
    with open('./Exported_Data/Category_CSVs/' + csv_filename,'a+', newline='', encoding='utf-8') as csv_file:
        book_csv = csv.writer(csv_file, delimiter=';')
        book_csv.writerow(info)

#create Cover Pages folder within Extracted_Data folder and write images as.jpg to new folder based on category
def download_images(title, UPC, img_url, category_name):
    img_directory = 'Exported_Data/Cover_Pages/'
    img_category_dir = img_directory + category_name + '/'
    img_cleaned = ''.join([x for x in title[:100] if x.isalnum() or x in ' ']).replace(' ', '_') + '.jpg'
    img_filename = 'UPC' + '_' + img_cleaned
    img_data = requests.get(img_url).content

    if not os.path.isdir(img_directory):
        os.mkdir(img_directory)
    img_path = os.path.join(img_category_dir, img_filename)
    if not os.path.isdir(img_category_dir):
        os.mkdir(img_category_dir)
    file = open(img_path, 'wb')
    file.write(img_data)