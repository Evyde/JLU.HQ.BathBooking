from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json
import MessageSender


def book(student_name="", student_phone="", student_sex="", student_time=0, student_id=0, bath_id=1):
    op = webdriver.ChromeOptions()
    # op.add_argument('headless') # run in background
    driver = webdriver.Chrome(options=op)
    driver.get('http://hqserver.jlu.edu.cn/yuci.php?xy=addxiyu1&from=singlemessage')

    # select place
    bath = driver.find_elements_by_xpath("//*[@href]")
    bath[bath_id-1].click()

    # select date
    date = driver.find_elements_by_xpath("//*[@href]")
    date[0].click()

    # select time
    times = driver.find_elements_by_xpath("//*[@href]")
    idx = int(student_sex) - 1 + (int(student_time) - 1) * 2
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
    driver.find_element_by_css_selector("input[type='radio'][value='" + student_sex + "']").click()

    # click the submit button
    submit = driver.find_element_by_id('Submit')
    # time.sleep(5)
    submit.click()

    # confirm to book
    alert = driver.switch_to.alert
    alert.accept()
    # alert.dismiss()
    # check if book success
    text = driver.find_element_by_xpath("/html/body/div/table/tbody/tr[1]/td/span").text
    if "预约成功" in text:
        # save screenshot with time stamp
        time_now = time.strftime("%Y-%m-%d %H:%M:%S")
        driver.save_screenshot('./bath-booking' + time_now + '.png')
        driver.quit()
        return True
    driver.quit()
    return False


with open('./student.json', encoding="utf-8") as json_file:
    d = json.load(json_file)
    m = MessageSender.MessageSender("bark")
    m.config({'apikey': ""})
    for data in d:
        try:
            while not book(data['name'], data['phone'], data['sex'], data['time'], data['id'], data['bathID']):
                pass
        except:
            if not book(data['name'], data['phone'], data['sex'], data['time'], data['id'], data['bathID']):
                msg = {"title": data['name'] + "预约失败！", "content": "时间：" + time.strftime("%Y-%m-%d %H:%M:%S")}
            else:
                msg = {"title": data['name'] + "预约成功！", "content": "时间：" + time.strftime("%Y-%m-%d %H:%M:%S")}
        else:
            # 结果推送到手机上
            msg = {"title": data['name']+"预约成功！", "content": "时间："+ time.strftime("%Y-%m-%d %H:%M:%S")}
        m.send(msg)
