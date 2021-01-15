import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class TestClass():

    driver = None

    def __init__(self):
        options = Options()
        options.headless = False
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    def buy_cooperate_data(self, recipient_name, recipient_number):
        try:
            driver.get("https://mymtn.com.ng/buybundles")
            time.sleep(2.5)

            driver.find_element_by_xpath(
                '//*[@id="wht-crv"]/div/div/app-buybundle-submenu/div[1]/div/ol/li[2]').click()
            time.sleep(0.5)

        except:
            print("Poor Network Connection")

        try:
            time.sleep(0.5)
            driver.find_element_by_xpath(
                "//*[@id='wht-crv']/div/div/app-buybundle-submenu/div[1]/div/div/div/a[8]").click()
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
            element = self.driver.find_element_by_xpath('//*[@id="mat-radio-9"]/label/div[1]')
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
            self.driver.find_element_by_xpath('//*[@id="feedbackmsg"]').send_keys(recipient_number)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="shownxt"]/div[9]/app-mainbutton').click()

            time.sleep(1.5)  # confirm button
            self.driver.find_element_by_xpath(
                '//*[@id="tat"]/app-smesuccess/div/div[1]/div/div/div/app-mainbutton').click()

        except:
            print("Poor Internet Connection")
