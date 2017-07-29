import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome('./assets/chromedriver')
driver.get('http://imdb.com/chart/top')


"""
shallow scrape:
	name, year, movie_ratings
"""

print('Starting shallow scrape...')

movie_names = driver.find_elements_by_css_selector('td.titleColumn > a')
# print(movie_names)
movie_years = driver.find_elements_by_class_name('secondaryInfo')
movie_ratings = driver.find_elements_by_css_selector('td.imdbRating > strong')

outputFile = open('movie_details_shallow.csv', 'w', newline='')
outputWriter = csv.writer(outputFile)
outputWriter.writerow(['Name', 'Release Year', 'Rating'])
for name, year, rating in zip(movie_names, movie_years, movie_ratings):
	outputWriter.writerow([name.text, year.text, rating.text])

outputFile.close()
  
driver.close()