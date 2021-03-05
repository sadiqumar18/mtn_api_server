import datetime
import json

import requests
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
import threading

options = Options()
options.headless = False
options.add_argument('--no-sandbox')
options.add_argument("--incognito")
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--blink-settings=imagesEnabled=false')

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver = webdriver.Firefox(options=options, executable_path=r"./geckodriver.exe")


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
        driver.get("https://mymtn.com.ng/buybundles/sponsoredwebpass")
        time.sleep(2)

        # driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/ol/li[2]').click()
        # time.sleep(0.5)

    except:
        print("failed to load data bundle page")

    """ Chooses the cooperate data gifting plan and fills the receipient's details """

    # getting the bundle
    try:

        driver.find_element_by_xpath(
            "//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[2]/app-sponsoredwebpass/div/div[2]/div[2]").click()

        # enter name
        driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(name)
        # validity
        try:
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mat-radio-5"]/label/div[1]').click()
        except:
            print("unable to click validity")

        try:
            el = driver.find_element_by_id("traffic")
            for option in el.find_elements_by_tag_name('option'):
                print(option.text)
                if option.text == "Internet/default option":
                    option.click()
        except:
            print('unable to click dropdown')

        # # recipient name
        # driver.find_element_by_xpath(
        #   "//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[2]/app-sponsoredwebpass/div/div[2]/div[2]").click()
        #
        # driver.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(name)
        # time.sleep(4)
        # # validity for 30days
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="mat-radio-8"]/label/div[1]').click()
        # time.sleep(1)
        try:
            time.sleep(2)
            element = driver.find_element_by_xpath(data_switcher(bundle))
        except:
            print("unable to click bundle")

        driver.execute_script("arguments[0].click();", element)

        # filling recipient numbers and confirmation process

        driver.find_element_by_xpath('//*[@id="feedbackmsg"]').send_keys(number)
        time.sleep(5)
        buttons = driver.find_elements_by_xpath("//*[contains(text(), 'Proceed')]")[0].click()

        # for btn in buttons:
        #     btn.click()

        print('about to click')

        time.sleep(3)  # confirm button
        print('about to click')

        driver.find_elements_by_xpath("//*[contains(text(), 'Confirm')]")[1].click()



        try:
            time.sleep(2)
            response = driver.find_element_by_xpath('//*[@id="Grid"]/div[3]')
            sendWebhook("https://zealvend.com/api/python_server",
                        {"status": "success", "number": number, "reference": reference, "message": response.text}
                        )

        except:
            sendWebhook("https://zealvend.com/api/python_server",
                        {"status": "success", "number": number, "reference": reference}
                        )
            print("failed to get response")

    except:
        print("failed to send")
        sendWebhook("https://zealvend.com/api/python_server",
                    {"status": "failed", "number": number, "reference": reference}
                    )


def subscribe_multiple(name, number, bundle, reference, first, last):
    """ Goes straight to the buybundles page """

    print(first)

    try:
        driver.get("https://mymtn.com.ng/buybundles/sponsoredwebpass")
        time.sleep(2)

        # driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/ol/li[2]').click()
        # time.sleep(0.5)

    except:
        print("failed to load data bundle page")

    """ Chooses the cooperate data gifting plan and fills the receipient's details """

    # getting the bundle
    try:

        driver.find_element_by_xpath(
            "//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[2]/app-sponsoredwebpass/div/div[2]/div[2]").click()

        # enter name
        driver.find_element_by_xpath('//*[@id="mat-input-1"]').send_keys(name)
        # validity
        try:
            time.sleep(2)
            driver.find_element_by_xpath('//*[@id="mat-radio-5"]/label/div[1]').click()
        except:
            print("unable to click validity")

        try:
            time.sleep(2)
            element = driver.find_element_by_xpath(data_switcher(bundle))
        except:
            print("unable to click bundle")

        driver.execute_script("arguments[0].click();", element)

        # filling recipient numbers and confirmation process

        driver.find_element_by_xpath('//*[@id="feedbackmsg"]').send_keys(number)
        time.sleep(8)
        driver.find_element_by_xpath('//*[@id="shownxt"]/div[9]/app-mainbutton').click()

        time.sleep(0.2)  # confirm button
        driver.find_element_by_xpath('//*[@id="tat"]/app-smesuccess/div/div[1]/div/div/div/app-mainbutton').click()

        try:
            time.sleep(10)
            response = driver.find_element_by_xpath('//*[@id="Grid"]/div[3]')
            sendWebhook("https://zealvend.com/api/python_server2",
                        {"status": "success", "number": number, "reference": reference, "message": response.text,
                         "first": first, "last": last,"bundle":bundle}
                        )
            print( {"status": "success", "number": number, "reference": reference, "message": response.text,
                    "first": first, "last": last,"bundle":bundle})

        except:
            sendWebhook("https://zealvend.com/api/python_server2",
                        {"status": "success", "number": number, "reference": reference, "message": response.text,
                         "first": first, "last": last,"bundle":bundle}
                        )
            print("failed to get response")

    except:
        print("failed to send")
        sendWebhook("https://zealvend.com/api/python_server2",
                    {"status": "failed", "number": number, "reference": reference,
                     "first": first, "last": last,"bundle":bundle}
                    )



def countdown():
    '''This function counts down after 5mins and click the website inorder to prevent it from logging out'''
    print("here")
    driver.find_element_by_xpath(
        '//*[@id="tat"]/app-buybundles/div/app-header/nav/div[1]/div/div/ul/li/a').click()  # element it clicks


# PLEASE NOTE: For the sake of this script, user variables are pre-defined

def refreshes():
    # driver.find_element_by_css_selector('body').send_keys(Keys.PAGE_DOWN)
    # driver.refresh();
    # driver.switch_to.window(driver.window_handles[0])
    try:
        element = driver.find_element_by_xpath("//a[text()='History']").click()
        driver.execute_script("arguments[0].click();", element)
    except:
        print("failde to refresh")


def data_switcher(bundle):
    switcher = {
        "MTN-500MB": '"mat-radio-9"',
        "MTN-1GB": '"mat-radio-10"',
        "MTN-2GB": '"mat-radio-11"',
        "MTN-3GB": '"mat-radio-12"',
        "MTN-5GB": '"mat-radio-13"'
    }

    print('//*[@id={data_string}]/label/div[1]'.format(data_string=switcher[bundle]))

    return '//*[@id={data_string}]/label/div[1]'.format(data_string=switcher[bundle])


def sendWebhook(url, data):
    requests.post(url, data=json.dumps(data), headers={"content-type": "application/json"})


def setInterval(func, minutes):
    e = threading.Event()
    while not e.wait(minutes):
        func()
