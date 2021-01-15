import json

import requests
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import threading

options = Options()
options.headless = False
options.add_argument('--no-sandbox')
# options.add_argument("--remote-debugging-port=9222")
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)


# number would be collected from user input
def login(number):
    try:
        # automated website of choice
        driver.get("https://mymtn.com.ng/")
        # time.sleep(10)

        # login
        driver.find_element_by_xpath("//*[@id='mat-input-0']").send_keys(number)
        driver.find_element_by_xpath("//*[@id='label']").click()
        # time.sleep(60)

        return "Login Successful"

    except:
        print("Poor internet connection")


# OTP Verification has to be done manually.


def subscribe(name, number, bundle, reference):
    """ Goes straight to the buybundles page """

    try:
        driver.get("https://mymtn.com.ng/buybundles")
        time.sleep(2.5)

        driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/ol/li[2]').click()
        time.sleep(0.5)

    except:
        print("failed to load data bundle page")

    """ Chooses the cooperate data gifting plan and fills the receipient's details """

    # getting the bundle
    try:
        time.sleep(0.5)
        driver.find_element_by_xpath("//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[1]/div/div/div/a[8]").click()
        time.sleep(0.5)

        # recipient name
        driver.find_element_by_xpath(
            "//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[2]/app-sponsoredwebpass/div/div[2]/div[2]").click()
        time.sleep(0.5)
        driver.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(name)

        # validity for 30days
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mat-radio-8"]/label/div[1]').click()
        time.sleep(1)

        element = driver.find_element_by_xpath(data_switcher(bundle))

        driver.execute_script("arguments[0].click();", element)

        # filling recipient numbers and confirmation process

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="feedbackmsg"]').send_keys(number)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="shownxt"]/div[9]/app-mainbutton').click()

        time.sleep(5)  # confirm button
        driver.find_element_by_xpath('//*[@id="tat"]/app-smesuccess/div/div[1]/div/div/div/app-mainbutton').click()
    except:
        print("failed to send")


def countdown():
    '''This function counts down after 5mins and click the website inorder to prevent it from logging out'''
    print("here")
    driver.find_element_by_xpath(
        '//*[@id="tat"]/app-buybundles/div/app-header/nav/div[1]/div/div/ul/li/a').click()  # element it clicks


# PLEASE NOTE: For the sake of this script, user variables are pre-defined


def data_switcher(bundle):
    switcher = {
        "MTN-1GB": '"mat-radio-13"',
        "MTN-2GB": '"mat-radio-14"',
        "MTN-3GB": '"mat-radio-15"',
        "MTN-5GB": '"mat-radio-16"'
    }

    return '//*[@id={data_string}]/label/div[1]'.format(data_string=switcher[bundle])


def sendWebhook(url, data):
    requests.post(url, data=json.dumps(data))


def setInterval(func, minutes):
    e = threading.Event()
    while not e.wait(minutes):
        func()
