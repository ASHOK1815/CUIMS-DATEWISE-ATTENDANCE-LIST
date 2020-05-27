from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver=webdriver.Chrome('C:\\Users\\ASUS\\Desktop\\driver\\chromedriver')

driver.get('https://uims.cuchd.in/uims/')

driver.find_element_by_id('txtUserId').send_keys('uid')
driver.find_element_by_name('btnNext').click()
driver.find_element_by_id('txtLoginPassword').send_keys('pass')
driver.find_element_by_name('btnLogin').click()

driver.get('https://uims.cuchd.in/UIMS/frmStudentCourseWiseAttendanceSummary.aspx')




driver.find_element_by_id("drpfilter").click()
select_fr = Select(driver.find_element_by_id("drpfilter")) 
driver.implicitly_wait(10)
select_fr.select_by_index(1)
print(select_fr)
driver.implicitly_wait(10)
driver.find_element_by_id("txtfromdate").send_keys('04/23/2020')
driver.find_element_by_id("txttodate").send_keys('04/25/2020')
driver.find_element_by_xpath("/html/body/form/div[4]/div[3]/div/div[8]/div[3]/input").click()




