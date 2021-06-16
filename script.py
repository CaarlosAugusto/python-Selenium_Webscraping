import requests
import bs4
import time
#Code to how search something in python using selenium anc coverting to bs4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
#get website url
url = 'https://www.youtube.com'
#ask user what theme him want to search
theme = input("What's theme you want to see the 3 videos most viewed in Youtube? ")
#define path mozilla and inicialize the WebDriver
binary = FirefoxBinary("C:\\Program Files\\Mozilla Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary, executable_path=r"C:\\geckodriver.exe")

driver.get(url)
#submit the theme
search_input = driver.find_elements_by_id("search")[1]
search_input.send_keys(theme)
time.sleep(5)
search_button = driver.find_element_by_id("search-icon-legacy")
search_button.click()
time.sleep(5)
#filter the most viewed videos
url = str(driver.current_url) + '&sp=CAM%253D'
driver.get(url)
time.sleep(5)
#get the page source
soup = bs4.BeautifulSoup(driver.page_source, 'lxml')
#find title, how many it was posted and views number
mylist = []
for i in range(1,4):
    div = soup.select("#title-wrapper")
    a = div[i].select("a")
    mylist.append(a[0].get('aria-label'))
#organize informations, separe title from numbers informations
driver.close()
list_name = []
info = []
for each in mylist:
    text = each.split(" ")
    max_length = len(text)
    name = ''
    information = ''
    for each in text[:-10]:
        name = name + each + " "
    list_name.append(name)
    for each in text[-10:]:
        information = information + each + " "
    info.append(information)
#show the results
print("Resultados: ")
for i in range(0,3):
    print("Video name: {}\nUpload data and views: {}\n".format(list_name[i], info[i]))
    i+=1
