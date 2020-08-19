from selenium import webdriver
import time

#This path is for chrome:
driver = webdriver.Chrome(executable_path="C:/Users/amirulcse/PycharmProjects/SeleniumProject/drivers/chromedriver.exe")

#This path is for firefox:
driver = webdriver.Firefox(executable_path="C:/Users/amirulcse/PycharmProjects/SeleniumProject/drivers/geckodriver.exe")
driver.get("http://google.com")

driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_name("q").send_keys("selenium")
time.sleep(2)
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
print("The test is completed successfully!!")