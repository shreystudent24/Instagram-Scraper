#import some necessory files, using time and selenium
import time
import webbrowser
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

#Set up Connections
PROXY =  "proxy.soax.com:10002"

PATH = "./chromedriver"
options = webdriver.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))
driver = webdriver.Chrome(service = Service(PATH),options=options)


#Open Instagram and Login in it. 
driver.get("https://www.instagram.com/login")

#target usename section to add username to the username section
username = WebDriverWait(driver, 10).until(EC.element_to_beclickable((By.CSS_SELECTOR, "input=[name=username]")))
password = WebDriverWait(driver, 10).until(EC.element_to_beclickable((By.CSS_SELECTOR, "input=[name=password]")))






