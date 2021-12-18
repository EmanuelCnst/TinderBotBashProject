from selenium import webdriver
from time import sleep
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
import pickle
import getpass
from secrets import username, password
geoEnable = webdriver.FirefoxOptions()

class TinderBot():

    def __init__(self):
        #profile = webdriver.FirefoxProfile(
        #    'C:\\Users\\EmanuelConstanti\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\3w9rvhtc.default')

        #profile.set_preference("dom.webdriver.enabled", False)
        #profile.set_preference('useAutomationExtension', False)
        #profile.update_preferences()
        #desired = DesiredCapabilities.FIREFOX

        #self.driver = webdriver.Firefox(firefox_profile=profile,
                           #desired_capabilities=desired)
        #self.driver = webdriver.Chrome(executable_path="D:\\QSync\\Workspace\Python\\TestSelenium\\chromedriver.exe")
        geoEnable.set_preference('geo.enabled', True)
        geoEnable.set_preference('geo.provider.use_corelocation', True)
        geoEnable.set_preference('geo.prompt.testing', True)
        geoEnable.set_preference('geo.prompt.testing.allow', True)
        self.driver = webdriver.Firefox(executable_path='D:\QSync\Workspace\Python\Tinder\geckodriver.exe')

        self.driver.implicitly_wait(10)

        #self.driver = webdriver.Chrome(chrome_options=chrome_options)


    def login(self):
        print('=== Facebook Login ===')
        self.driver = self.driver
        self.driver.get('https://www.facebook.com/')
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-testid="cookie-policy-banner-accept"]'))) 
            element.click()
        except:
            pass

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
        self.driver.find_element_by_css_selector('[data-testid="royal_login_button"]').submit()
        sleep(6)

               
        #Call Website tinder
        self.driver.get('https://tinder.com')
        sleep(2)

         #####TEST TESR 
        mainpage =  self.driver.current_window_handle
        print(mainpage)
        sleep(5)

        ameldebtn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')  
        ameldebtn.click()
        
        sleep(2)
        googlebtn = self.driver.find_element_by_css_selector('div.My\(10px\):nth-child(2) > button:nth-child(1)')
        googlebtn.click()

        print('Login Worked Hooray')

        self.driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()

        # allow use your geolocation
        sleep(4)
        self.web_driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[1]"
        ).click()

        # disable notification at web application
        self.web_driver.find_element_by_xpath(
            "/html/body/div[2]/div/div/div/div/div[3]/button[2]"
        ).click()

        print('It works')

        

           


bot = TinderBot()
bot.login()
