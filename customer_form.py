import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select

# Variable Definition
wait_time = 6
url = "https://automationplayground.com/crm/login.html"
email = "animashaunfatimah02@gmail.com"
password = "getthisdone"
new_email = "fateemah12@yopmail.com"
first_name = "Ayomide"
last_name = "Bello"
city_name = "Seattle"
state = "Washington"

# Browser Initialization
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(wait_time)

# Login Process
Email = driver.find_element(By.ID, "email-id")
Email.send_keys(email)

PassWord = driver.find_element(By.ID, "password")
PassWord.send_keys(password)

# Optionally, check the "Remember me" checkbox
remember_me_checkbox = driver.find_element(By.CLASS_NAME, "checkbox")
remember_me_checkbox.click()

Submit = driver.find_element(By.ID, "submit-id")
Submit.click()

#time.sleep(wait_time)

# Click on "New Customer"
NewCustomer = driver.find_element(By.ID, "new-customer")
NewCustomer.click()

# Fill out New Customer Form
New_Email = driver.find_element(By.ID, "EmailAddress")
New_Email.send_keys(new_email)

First_Name = driver.find_element(By.ID, "FirstName")
First_Name.send_keys(first_name)

Last_Name = driver.find_element(By.ID, "LastName")
Last_Name.send_keys(last_name)

City_ = driver.find_element(By.ID, "City")
City_.send_keys(city_name)

State_or_Region = driver.find_element(By.ID, "StateOrRegion")
State = Select(State_or_Region)
State.select_by_visible_text("Washington")

Gender_options = driver.find_elements(By.NAME, "gender")
Gender_options[1].click()

Submit = driver.find_element(By.CLASS_NAME, "btn-primary")
Submit.click()

time.sleep(3)

# Close the browser
driver.quit()
