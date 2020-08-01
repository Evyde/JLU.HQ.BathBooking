from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json

student_name = ""
student_phone = ""
student_sex = "" # 1 for male, 2 for female
student_time = 0

with open('./student.json') as json_file:
    data = json.load(json_file)
    student_name = data['name']
    student_phone = data['phone']
    student_sex = data['sex']
    student_time = data['time']

op = webdriver.ChromeOptions()
op.add_argument('headless') # run in background
driver = webdriver.Chrome(options=op)
bath_search = driver.get('http://hqserver.jlu.edu.cn/yuci.php?xy=xiyucha')

# fill name
name = driver.find_element_by_name("k")
name.send_keys(student_name)
# fill mobile phone number
phone = driver.find_element_by_name("p")
phone.send_keys(student_phone)

# select place
select_bath = Select(driver.find_element_by_name("x"))
select_bath.select_by_value("1")

# select date
select_date = Select(driver.find_element_by_name("d"))
select_date.select_by_index(1)

# select time
select_time = Select(driver.find_element_by_name("o"))
t = student_time-14+1
select_time.select_by_index(t)

# select sex
select_sex = Select(driver.find_element_by_name("s"))
select_sex.select_by_value(student_sex)

#  time.sleep(100)

# click search button
btn_search = driver.find_element_by_name("Submit")
btn_search.click()

time.sleep(1)

# save screenshot with time stamp
time_now = time.strftime("%Y-%m-%d %H:%M:%S")
driver.save_screenshot('./bath-booking'+time_now+'.png')
driver.quit()
