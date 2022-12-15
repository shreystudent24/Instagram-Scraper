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
username = WebDriverWait(driver, 10).until(EC.element_to_beclickable((By.CSS_SELECTOR, "input=[name=username")))
password = WebDriverWait(driver, 10).until(EC.element_to_beclickable((By.CSS_SELECTOR, "input=[name=password")))

#enter the details of username and password
    #Send keys to pass the arguments. 
username.clear()
username.send_keys("Enter your userName")
password.clear()
password.send_keys("Enter your password")

#hit login button

button = WebDriverWait(driver, 10).until(EC.element_to_beclickable((By.CSS_SELECTOR, "input=[type='submit']")))
button.click()

#target seach box and ennter input into it.
searchbox = WebDriverWait(driver, 10).until(EC.element_to_beclickable((By.XPATH, "//input=[@placeholder='Search']")))
searchbox.clear()

keyword = "#bikes"     #you can enter your desirable keyword
searchbox.send_keys(keyword)

#wait for 5 seconds
time.sleep(5)
searchbox.send_keys(keys.ENTER)  #this is press enter on keyboard

#have to press enter two times to land to a search page. 
time.sleep(5)
searchbox.send_keys(keys.ENTER)


#scroll down for more images
driver.execute.script("window.scrollTo(0,4000);")

#taget image
time.sleep(5)
images = driver.find_elements(By.TAG_NAME, 'img')
images = [images.get_attribute('src') for image in images]
images = images[:-2]

#no of images linked
print("Totol number of scrapped images: ", len(images))

#display targeted image 
print("Displaying Images: ", images[4])
driver.get(images[4])









