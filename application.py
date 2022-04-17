from time import sleep
import json

from selenium import webdriver
import chromedriver_binary

def main():
    data = json.load(open('data.json', 'r'))

    driver = webdriver.Chrome()
    driver.get(data["url"])

    driver.find_element_by_xpath('//*[@id="c_q12"]').send_keys(data["name"])
    driver.find_element_by_xpath('//*[@id="c_q14"]').send_keys(data["name_kana"])
    driver.find_element_by_xpath('//*[@id="c_q2"]').send_keys(data["email"])
    driver.find_element_by_xpath('//*[@id="c_q2_confirm"]').send_keys(data["email"])
    driver.find_element_by_xpath('//*[@id="c_q9"]').send_keys(data["id"])
    for date_i in range(5):
        driver.find_element_by_xpath(f'//*[@id="c_q10_{date_i}"]').click()
    driver.find_element_by_xpath('//*[@id="c_q15_0"]').click()
    sleep(68)

    driver.find_element_by_xpath('//*[@id="wcf5start"]').click()
    sleep(13)
    
    driver.find_element_by_xpath('//*[@id="confirm"]').click()


if __name__ == "__main__":
    main()


