#import libraries needed
import os
import csv
import requests

#Create Exported_Data folder as well as .csv file within new folder
def create_csv_file(csv_filename):
    csv_directory = 'Exported_Data/Category_CSVs'
    if not os.path.isdir(csv_directory):
        os.mkdir(csv_directory)
    with open('./Exported_Data/Category_CSVs/' + csv_filename, 'w', newline='', encoding-'utf-8') as csv_file:
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