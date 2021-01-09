from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from webdriver_manager.utils import ChromeType



options = Options()
options.headless = False
#options.add_argument('--no-sandbox')
#options.add_argument("--remote-debugging-port=9222")
driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install(), options=options)


# number would be collected from user input
def login(number):
    try:
        # automated website of choice
        driver.get("https://mymtn.com.ng/")
        #time.sleep(10)

        # login
        driver.find_element_by_xpath("//*[@id='mat-input-0']").send_keys(number)
        driver.find_element_by_xpath("//*[@id='label']").click()
        #time.sleep(60)

        return "Login Successful"

    except:
        print("Poor internet connection")


# OTP Verification has to be done manually.


def subscribe(recipient_name, recipient_number):
    print(recipient_number)
    """ Goes straight to the buybundles page """

    try:
        driver.get("https://mymtn.com.ng/buybundles")
        time.sleep(2.5)

        driver.find_element_by_xpath('//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/ol/li[2]').click()
        time.sleep(0.5)

    except:
        print("Poor Network Connection")


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
        driver.find_element_by_xpath('//*[@id="mat-input-2"]').send_keys(recipient_name)

        # validity for 30days
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="mat-radio-8"]/label/div[1]').click()
        time.sleep(1)

        # data type (50MB)
        element = driver.find_element_by_xpath('//*[@id="mat-radio-9"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        '''LIST OF DATA BUNDLES
        # 500 MB: element = driver.find_element_by_xpath('//*[@id="mat-radio-12"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        # 1GB: element = driver.find_element_by_xpath('//*[@id="mat-radio-13"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        # 2GB: element = driver.find_element_by_xpath('//*[@id="mat-radio-14"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        # 3GB: element = driver.find_element_by_xpath('//*[@id="mat-radio-15"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        # 5GB: element = driver.find_element_by_xpath('//*[@id="mat-radio-16"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        # OTHERS: element = driver.find_element_by_xpath('//*[@id="mat-radio-6"]/label/div[1]')
        driver.execute_script("arguments[0].click();", element)

        if option == "Others:
            amount = input("Enter data amount in GB: ")
            driver.find_element_by_xpath(//*[@id="mat-input-3"]).sendkeys(amount)
        '''

        # filling recipient numbers and confirmation process

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="feedbackmsg"]').send_keys(recipient_number)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="shownxt"]/div[9]/app-mainbutton').click()

        time.sleep(1.5)   # confirm button
        driver.find_element_by_xpath('//*[@id="tat"]/app-smesuccess/div/div[1]/div/div/div/app-mainbutton').click()

    except:
        print("Poor Internet Connection")

def countdown(t):
    '''This function counts down after 5mins and click the website inorder to prevent it from logging out'''

    while t:  #countdown loop
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time.sleep(1)
        t -= 1
    driver.find_element_by_xpath('//*[@id="tat"]/app-buybundles/div/app-header/nav/div[1]/div/div/ul/li/a').click()  #element it clicks
# PLEASE NOTE: For the sake of this script, user variables are pre-defined

