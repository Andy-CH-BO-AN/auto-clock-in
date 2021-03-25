import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

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
    driver.find_element_by_id('clockin').click()


def offline():
    driver.find_element_by_id('clockout').click()


def select_action():
    choice = input('按0上班卡，按1下班卡：')
    if int(choice) == 0:
        online()
    elif int(choice) == 1:
        offline()
    else:
        raise Exception('請重新選擇')


if __name__ == '__main__':
    main()
    driver.quit()
