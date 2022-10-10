# -*- coding: utf-8 -*-

from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By
import ssl
import requests


def google_scroll(SCROLL_PAUSE_TIME,search):
    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = SCROLL_PAUSE_TIME

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            try:
                driver.find_element(By.CSS_SELECTOR, ".mye4qd").click()
            except:
                break
        last_height = new_height

def url_retrieve(copied_xpath, total_image_count):
    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")
    print(f'{"*"*50}Crawlling started.{"*"*50}')
    count = 1
    for image in images:
        try:
            try:
                image.click()
            except:
                try:
                    driver.execute_script("arguments[0].click();", image)
                except:
                    pass
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,
                                         copied_xpath).get_attribute('src')
            r = requests.get(imgUrl)
            with open(f"{search}/" + search + "_" + str(count) + ".jpg", mode="wb") as f:
                f.write(r.content)

            print(f"Image saved: {search}_{count}.jpg")
            # we can not use enumerate function. because there are passed case.
            if (count == total_image_count):
                break
            else:
                count+=1
        except Exception as e:
            print(e)
            pass
    print(f'{"*"*50}Crawlling Completed.{"*"*50}')
    driver.close()

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context

    PATH = "./chromedriver"
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

    search = input('Please enter a search term: ')
    total_image_count = int(input('Enter the total number: '))

    if not os.path.isdir(f"{search}/"):
        os.makedirs(f"{search}/")

    copied_xpath='//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'

    google_scroll(SCROLL_PAUSE_TIME=1, search=search)
    url_retrieve(copied_xpath=copied_xpath, total_image_count=total_image_count)
