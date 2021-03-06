import json
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import datetime
import time
import random

chrome_path = ChromeDriverManager().install()
driver = webdriver.Chrome(chrome_path)
clock_in = '/html/body/div[1]/div[3]/div/div[1]/div[5]/div[1]/div/div[2]/div[1]/div[1]/div'
clock_out = '/html/body/div[1]/div[3]/div/div[1]/div[5]/div[1]/div/div[2]/div[1]/div[2]/div'
clock = '/html/body/div[1]/div[3]/div/div[1]/div[5]/div[1]/div/div[1]/div[3]/div[1]'


def check_time(now=datetime.datetime.now()):
    if now.weekday() <= 4:
        with open('holiday.txt', 'r') as f:
            for line in f.readlines():
                if now.strftime("%Y-%m-%d") == line.replace('\n', ''):
                    print('holiday')
                    return 'holiday'
        print('work')
        return 'work'
    else:
        with open('workday.txt', 'r') as f:
            for line in f.readlines():
                if now.strftime("%Y-%m-%d") == line.replace('\n', ''):
                    print('work')
                    return 'work'
        print('holiday')
        return 'holiday'


def main():
    if check_time() == 'holiday':
        driver.quit()
        log("It's holiday!!")
        sys.exit()
    else:
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
    driver.find_element_by_xpath(clock_in).click()
    log('clockin')


def offline():
    driver.find_element_by_xpath(clock_out).click()
    log('clockout')


def select_action():
    WebDriverWait(driver, 5, 0.5). \
        until(ec.visibility_of_element_located((By.XPATH, clock)))
    parameter = sys.argv[1]
    if int(parameter) == 0:
        time.sleep(random_wait)
        online()
    elif int(parameter) == 1:
        time.sleep(random_wait)
        offline()
    elif int(parameter) == 2:
        log("testing")
    else:
        log(Exception('something went wrong'))
        raise Exception('something went wrong')


def log(status):
    with open('log.txt', 'a') as f:
        f.write(f'\n{datetime.datetime.now()} {status}')
        f.close()


if __name__ == '__main__':
    random_wait = random.randint(0, 120)
    print(random_wait)
    try:
        main()
    except Exception as E:
        log(f"Error:{E}")
    time.sleep(1)
    driver.quit()
