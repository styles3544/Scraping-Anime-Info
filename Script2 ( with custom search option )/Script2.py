from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
import time
import sys

url = "https://next-episode.net/"


# search query
query = raw_input("enter the name of anime: ")

# Absolute path of your chrome driver
chromedriver_path = "./chromedriver"

# For running chrome in background add the following lines defining headless in options
chrome_options = Options()
chrome_options.add_argument("--headless")

webdriver = webdriver.Chrome(
    executable_path = chromedriver_path,
    options = chrome_options
)

with webdriver as driver:
    # timeout
    wait = WebDriverWait(driver, 10)

    # extract data
    driver.get(url)

    # finding the search box and type the query and presses enter
    search_box = driver.find_element_by_xpath('//*[@id="searchf"]')
    search_box.send_keys(query + Keys.RETURN)

    # wait
    time.sleep(5)

    # results
    results = driver.find_elements_by_class_name("tdc2")

    #source = driver.page_source  ---> after this line I can use beautiful soup


    for items in results:
        itemArr = items.text 
        print (itemArr)
        print("\n")

    driver.close()


