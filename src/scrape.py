from selenium import webdriver
import time


# create web driver to control browser
driver = webdriver.Chrome('./assets/chromedriver')

# open our webpage in a browser
driver.get('file:///home/tomisin/Documents/projects/Web%20Scraping/NDev/src/index.html')


outer_div = driver.find_element_by_id('outer')
outer_color = outer_div.value_of_css_property("background-color")
print(outer_color)


info1 = driver.find_element_by_css_selector('#info1')
print(info1.text)


intro2 = driver.find_element_by_xpath('//*[@id="outer"]/div[2]/h1')
print(intro2.text)


password = driver.find_element_by_id('pwd')
time.sleep(10)															# waits so you can type in a password
print(password.get_attribute('value'))			# boom! security risk


# end the session
driver.close()