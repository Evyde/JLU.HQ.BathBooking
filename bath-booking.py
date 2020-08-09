from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json

student_name = ""
student_phone = ""
student_id = ""
student_sex = "" # 1 for male, 2 for female
student_time = 0

with open('/home/tlss/student.json') as json_file:
    data = json.load(json_file)
    student_name = data['name']
    student_phone = data['phone']
    student_id = data['id']
    student_sex = data['sex']
    student_time = data['time']

op = webdriver.ChromeOptions()
# op.add_argument('headless') # run in background
driver = webdriver.Chrome(options=op)
driver.get('http://hqserver.jlu.edu.cn/yuci.php?xy=addxiyu1&from=singlemessage')

# select place
bath = driver.find_elements_by_xpath("//*[@href]")
bath[0].click()

# select date
date = driver.find_elements_by_xpath("//*[@href]")
date[0].click()

# select time
times = driver.find_elements_by_xpath("//*[@href]")
idx = int(student_sex)-1 + (int(student_time)-1)*2
times[idx].click()

# fill name
textbox_name = driver.find_element_by_name("name")
textbox_name.send_keys(student_name)
# fill phone
textbox_phone = driver.find_element_by_name("mobile")
textbox_phone.send_keys(student_phone)
# fill student id
textbox_id = driver.find_element_by_name("xuehao")
textbox_id.send_keys(student_id)

# select sex, default male
sexs = driver.find_element_by_css_selector("input[type='radio'][value='"+student_sex+"']").click()

# click the submit button
submit = driver.find_element_by_id('Submit')
# time.sleep(5)
submit.click()

# confirm to book
alert = driver.switch_to.alert
alert.accept()
# alert.dismiss()

time.sleep(1)

driver.quit()
