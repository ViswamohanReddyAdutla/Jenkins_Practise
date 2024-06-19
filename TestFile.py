from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximized')
driver=webdriver.Chrome(options=chrome_options)
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//input[@name='username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
msg=driver.find_element(By.XPATH,"//span[@class='oxd-topbar-header-breadcrumb']/h6").text
driver.close()
assert msg=="Dashboard", "Msg is not matching our expectations"
