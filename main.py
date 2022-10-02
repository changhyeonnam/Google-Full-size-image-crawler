from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys
import time
import urllib.request
import os
from selenium.webdriver.common.by import By


if __name__ == '__main__':
    if not os.path.isdir("nike/"):
        os.makedirs("nike/")
    PATH="./chromedriver"
    driver = webdriver.Chrome(executable_path=PATH)
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")

    search = "nike"
    elem = driver.find_element(By.NAME,"q")
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
                driver.find_element(By.CSS_SELECTOR,".mye4qd").click()
            except:
                break
        last_height = new_height

    images = driver.find_elements(By.CSS_SELECTOR,".rg_i.Q4LuWd")
    count = 1

    for image in images:
        try:
            image.click()
            time.sleep(2)
            imgUrl = driver.find_element(By.XPATH,"//*[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[3]/div/a/img").get_attribute('src')
            urllib.request.urlretrieve(imgUrl, "nike/" + search + "_" + str(count) + ".jpg")
            print("Image saved: nike_{}.jpg".format(count))
            count += 1
        except:
            pass

    driver.close()