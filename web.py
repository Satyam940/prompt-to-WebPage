from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()


driver.get("https://easyeats-yj2ftzt.gamma.site/")


try:
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    
    source = driver.page_source

   
    with open("source.html", "w", encoding="utf-8") as f:
        f.write(source)
finally:
    driver.quit()
