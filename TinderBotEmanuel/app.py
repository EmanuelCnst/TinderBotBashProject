# Author: EConstanti Robin Zweifel
# Date: 18.12.2021
# Login to facebook

from selenium import webdriver
from tinder.login.tinderlogin import TinderLogin
from tinder.tinderbot import TinderBot
geoEnable = webdriver.FirefoxOptions()

geoEnable.set_preference('geo.enabled', True)
geoEnable.set_preference('geo.provider.use_corelocation', True)
geoEnable.set_preference('geo.prompt.testing', True)
geoEnable.set_preference('geo.prompt.testing.allow', True)
driver =  webdriver.Firefox(options=geoEnable ,executable_path='D:\QSync\Workspace\Python\TinderBotEmanuel\geckodriver.exe')
login = TinderLogin(driver)
bot = TinderBot(driver)

print('=== TinderBot Start ===')
login.logIn()
if login.isLogged():
    print('=== Tinder Perform ===')
    while True:
        bot.perform()
else:
    print('Error: Failed to login to Tinder. Check your data or try later.')