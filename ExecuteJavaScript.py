from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Install chrome driver and create WebDriver object
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage
driver.get("https://google.com")
#Execute JavaScript to create an alert
script = "alert('Hello from Kamlesh')"
driver.execute_script(script)
# Switch to alert and accept it
alert = driver.switch_to.alert
print("Alert text: ", alert.text)
time.sleep(3)
alert.accept()
print("Page Title: ", driver.title)
driver.quit()
print("Test execution completed")