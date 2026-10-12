from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
sleep(3)
browser.get("https://www.instagram.com")
sleep(3)
search_box = browser.find_element("name", "username")
pass_box = browser.find_element("name", "password")
for char in "aihype3":       #gives the typing effect
    search_box.send_keys(char)
    sleep(0.2)
for char in "Aihype2005!":
    pass_box.send_keys(char)
    sleep(0.1)
sleep(2)
pass_box.send_keys(Keys.ENTER)
sleep(3)
first_short = browser.find_element("xpath", '//*[@id="mount_0_0_f6"]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[4]/span/div/a/div/div[1]/div/div/svg')
sleep(5)
first_short.click()
sleep(100)
# while True:
#     sleep(5)
#     next_button = browser.find_element("xpath", '//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]')
#     next_button.click()

# #hw insta short scroll
    