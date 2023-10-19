import requests
header = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36'}

def getDownload(url, param = None, retries = 3):
    resp = None
    try:
        resp = requests.get(url, params = param, headers = header)
        resp.raise_for_status()
    except requests.exceptions.HTTPError as e:
        if 500 <= resp.status_code < 600 and retries > 0:
            print('Retries : {0}'.format(retries))
            return getDownload(url, param, retries -1)
        else:
            print(resp.status_code)
            print(resp.reason)
            print(resp.request.headers)
            
    return resp

from bs4 import BeautifulSoup
from selenium import webdriver
import json
import re
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome("/Users/bluevisor/Documents/AI/ipynb/chromedriver")

url = "https://news.naver.com"
driver.get(url)

for tag in driver.find_elements_by_xpath("//span[@class='category_ranking']//a"):
    tag.click()
    getnews(tag.text)

def getnews(category):
    for tag in driver.find_elements_by_xpath("//div[@id='right.ranking_contents']//ul[@class='section_list_ranking']//a"):
        #print(tag.get_attribute("href"))
        url = tag.get_attribute("href")
        html = getDownload(url)
        dom = BeautifulSoup(html.text,"html.parser")
        
        title = []
        text = []
        
        for tag2 in dom.select("h3#articleTitle"):
            title = tag2.text
            print(title)
            
        for tag2 in dom.select("#articleBodyContents"):
            text = tag2.text
            
        category = category.replace("/","")
        f = open("Snews/" + category + "_" + url.split("aid=")[1].split("&")[0] +".txt", 'w')
        f.write(title + "\n")
        f.write(text)
        f.close()
        break
    