#import some necessory files, using time and selenium
import time
import webbrowser
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
options = webbrowser.ChromeOptions()
options.add_argument('proxy.soax.com'.format(PROXY))




