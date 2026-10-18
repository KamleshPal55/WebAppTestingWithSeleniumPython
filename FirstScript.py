from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver.get("https://www.selenium.dev")

# driver.get("https://google.com")
# driver.maximize_window()
# driver.implicitly_wait(10)
#
# googleSearchBox = driver.find_element(By.ID, "ti6dpd")
# googleSearchBox.send_keys("Selenium")
# googleSearchBox.send_keys(Keys.RETURN)
# driver.find_element(By.NAME, "btnK").click()

driver.get("https://trytestingthis.netlify.app/index.html")

driver.find_element(By.ID, "fname").send_keys("Kamlesh")
driver.find_element(By.ID, "lname").send_keys("Pal")
time.sleep(3)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
time.sleep(3)
driver.quit()
print("Done")


