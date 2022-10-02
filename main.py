from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    PATH = "./chromedriver"
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

    search = input('Please enter a search term: ')
    total_image_count = int(input('Enter the total number: '))

    if not os.path.isdir(f"{search}/"):
        os.makedirs(f"{search}/")

    elem = driver.find_element(By.NAME, "q")
    elem.send_keys(search)
    elem.send_keys(Keys.RETURN)

    SCROLL_PAUSE_TIME = 1

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

    images = driver.find_elements(By.CSS_SELECTOR, ".rg_i.Q4LuWd")

    copied_xpath='//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img'
    print(f'{"*"*50}Crawlling started.{"*"*50}')
    count = 1
    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,
                                         copied_xpath).get_attribute('src')
            urllib.request.urlretrieve(imgUrl, f"{search}/" + search + "_" + str(count) + ".jpg")
            print(f"Image saved: {search}_{count}.jpg")
            # we can not use enumerate function. because there are passed case.
            count+=1
            if (count == total_image_count+1):
                break
        except:
            pass
    print(f'{"*"*50}Crawlling Completed.{"*"*50}')
    driver.close()
