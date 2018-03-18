import requests
import json
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class InstagramCrawler:

    def __init__(self, driver, data):
        ## for log system
        print("\n********************************init*****************************************\n")
        print("Executing __init__\n")
        
        ## self variables

        # driver from scrapy
        self.driver = driver
        
        #json with account info
        self.data = data

        #url to access
        self.url = "https://www.instagram.com/"
        self.url_login = "https://www.instagram.com/accounts/login/?force_classic_login"

        #About followers
        self.qtdFol = 0
        self.followers = []
        

        ## for log system
        print("\n\n\tData:" + self.data['USERNAME'])
        print("\tURL:" + self.url)
        print("\n**********************************end******************************************\n")

    def login(self):
        print("\n*******************************************************************************\n")
        print("Executing login\n")
        self.driver.get(self.url_login)

        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.data['USERNAME'])
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.data['PASSWORD'])
        self.driver.find_element_by_xpath("//input[@type='submit']").click()

        # Wait for the login page to load
        try:
            WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.LINK_TEXT, "Instagram"))
                )
        except:
            print("\n\nLogin Fail!!!!")

        print("\n*******************************************************************************\n")
        
        return
        """
        try:
            self.driver.set_page_load_timeout(1)
        except Exception:
            return
        """
        
    def __click(self, scrape_type = "follower"):
        ## for log system
        print("\n********************************init*****************************************\n")
        print("Executing __click\n")

        self.driver.find_element_by_partial_link_text(scrape_type).click()
        
        ## scrape the followers/following accordingly
        #xpath = "//div[@role='dialog']//li//a"
        #xpath = "//div[@role='dialog']//a[1]"
        #xpath = "//li//a"
        #xpath = "html/body/div//li//a"
        #xpath = "/html/body/div[2]/div/div[2]/div/div[2]/ul/div/li["+str(2)+"]/div/div[1]/div/div[1]/a"
        
        xpath = "//a[@class='_2g7d5 notranslate _o5iw8']"
        span = self.driver.find_elements_by_xpath(xpath)
        
        #span = self.driver.find_elements_by_id("FollowListContainer")
        #span = self.driver.find_elements_by_class_name("_2g7d5 notranslate _o5iw8")
        print (span)
        
        print("\nSeguidores:")       
        for item in span:
              print (item.text)
              print("\n")
        
        print("\n**********************************end******************************************\n")

        return span

    def scrape(self):
        ## for log system
        print("\n********************************init*****************************************\n")
        print("Executing scrape\n")

        self.driver.get(self.url+self.data['USERNAME'])

        ## get number of followers
        self.qtdFol = int(self.driver.find_element_by_xpath("//li[2]/a/span").text)
        
        # get username of all the followers
        self.followers = self.__click("seguidor")
        
        ## for log system
        print("\n\n\tQtd of Followers:" + str(self.qtdFol))
        #print("\tFollowers:")
        #print (self.followers)
        print("\n**********************************end******************************************\n")

        
    def run(self):
        self.login()
        self.scrape()
    
def main():
    pass

if __name__ == "__main__":
    main()
