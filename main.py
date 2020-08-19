from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path="C:/Users/amirulcse/PycharmProjects/SeleniumProject/drivers/chromedriver.exe")

driver.get("http://google.com")

driver.maximize_window()

driver.find_element_by_name("q").send_keys("mask")
time.sleep(2)
driver.find_element_by_name("btnK").click()

print(driver.title)

driver.close()

print("Successfully Test Pass!!")