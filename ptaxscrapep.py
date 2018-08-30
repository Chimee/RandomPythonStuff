from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv
import requests

base_url = "http://cvb.manatron.com/Tabs/PropertySearch.aspx"
page_array = []

name = input("Enter the name to be searched: ")
nextpage = "aenabled ui-button ui-widget ui-state-default ui-button-text-only ui-corner-right ui-state-hover"
#SEARCH_BUTTON_XPATH = '//img[@title="Start Service"]'
driver = webdriver.Chrome(executable_path='C:/Users/ceze/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(base_url)
assert "Property Search" in driver.title
elem = driver.find_element_by_id("fldInput")
elem.send_keys(name)
#elem = driver.find_element_by_id("login_pwd")
elem.send_keys(Keys.RETURN)
assert "Property Search" in driver.title
#driver.find_element_by_xpath(START_BUTTON_XPATH).click()

source = driver.page_source




def next_page():
    npage = driver.find_element_by_css_selector("a.enabled.ui-button.ui-widget.ui-state-default.ui-button-text-only.ui-corner-right")
    npage.send_keys('\n')


def get_accounts():
    for node in soup.findAll('a', title='View Account Detail'):
        print (''.join(node.findAll(text=True)))
        with open(<path to output_csv>, "wb") as csv_file:
                writer = csv.writer(csv_file, delimiter=',')
                for line in data:
                    writer.writerow(line)

    
soup = BeautifulSoup(source, "html.parser")

time.sleep(2)


get_accounts()


time.sleep(2)

next_page()


time.sleep(2)

get_accounts()


