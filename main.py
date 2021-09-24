from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

INTERNET_SPEED_URL = 'https://www.speedtest.net/'
TWITTER_URL = 'https://twitter.com/i/flow/login'
PROMISED_DOWN = 100
PROMISED_UP = 100


linux_chrome_driver_path = '/home/cal/Developer/chromedriver'
#win_chrome_driver_path = 'C:\Developer\chromedriver.exe'

class InternetSpeedTwitterBot:
"""Identify current Interent Speeds on home network, sign-in to Twitter and Tweet ISP Provider"""

    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(INTERNET_SPEED_URL)
        test_speed = self.driver.find_element_by_class_name('start-text')
        test_speed.click()
        time.sleep(60)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                     '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/'
                                            'div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(5)
        sign_in = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                    '/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        #TWITTER_USER & TWITTER_PW saved as environment variables
        sign_in.send_keys(TWITTER_USER)
        next = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/'
                                                 'div[2]/div[2]/div[2]/div/div')
        next.click()
        time.sleep(5)
        password = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]'
                                                     '/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/div/label/div/d'
                                                     'iv[2]/div/input')
        password.send_keys(TWITTER_PW)
        login = self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/'
                                                  'div[2]/div/div/div[2]/div[2]/div[2]/div/div')
        login.click()
        time.sleep(5)
        tweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div'
                                                  '/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div'
                                                  '/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweet.send_keys(ISP_TWEET)
        send_tweet = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/di'
                                                       'v[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2'
                                                       ']/div[3]/div/span/span')
        send_tweet.click()




test = InternetSpeedTwitterBot(linux_chrome_driver_path)
test.get_internet_speed()
if float(test.down) < 100 or float(test.up) < 100:
    #Excluded actual ISP Provider's Twitter handle but can be added within Tweet below.
    ISP_TWEET = f"Hey internet provider, why is my download speed at {test.down} mbps and my upload speed at " \
                f"{test.up} mbps when I'm paying for {PROMISED_DOWN} mbps DL/{PROMISED_UP} mbps ul?"
    test.tweet_at_provider()
else:
    print("Internet speeds look good.")
test.driver.close()


