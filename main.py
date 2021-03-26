import json
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

chrome_path = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome_path)


def main():
    with open("config.json", "r") as f:
        info = json.load(f)
    print(info)
    url = info["url"]
    driver.get(url)
    login(info)


def login(info):
    driver.find_element_by_id('dept_input').send_keys(info["company id"])
    driver.find_element_by_id('username_input').send_keys(info['account'])
    driver.find_element_by_id('password-input').send_keys(info['password'])
    driver.find_element_by_id('login-button').click()
    select_action()


def online():
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div/div[1]/div[5]/div[1]/div/div[2]/div[1]/div[1]/div').click()


def offline():
    driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div/div[1]/div[5]/div[1]/div/div[2]/div[1]/div[2]/div').click()


def select_action():
    clock = '/html/body/div[1]/div[3]/div/div[1]/div[5]/div[1]/div/div[1]/div[3]/div[1]'
    WebDriverWait(driver, 5, 0.5). \
        until(ec.visibility_of_element_located((By.XPATH, clock)))
    parameter = sys.argv[1]
    if int(parameter) == 0:
        online()
    elif int(parameter) == 1:
        offline()
    elif int(parameter) == 2:
        print(8888888888888)
    else:
        raise Exception('請重新選擇')


if __name__ == '__main__':
    main()
    driver.quit()
