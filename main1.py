

from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,WebDriverException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options 
import time
from random import randint

from time import sleep
import requests as req
import os
import json
import sys
import re

#captcha_sleep is time to solve it. after that will go to game
#name you want to replace with @
#total number of links you have put in urls.txt
#limit how many comments you want to generate
#Enter your Login data here,
File = 'urls.txt'
nooflinks=2
Username = ''
Password = ''
name='@abdullah'
limit=26

#methods to read comments and print comments
def comments(driver,i,text):
    global limit
    count=limit
    comms = driver.find_elements_by_class_name('C4VMK')
    print ('Comments Found: ' + str(len(comms)))
    print ('Saving Comments...')
    Num = 1
    for one in comms:
        count-=1
        if count>=0:
            print (str(Num) + ' / ' + str(len(comms)))
            comment =  one.find_element_by_xpath('.//span').text.encode('utf-8')
            co=comment.decode('utf-8')
            replac=re.sub(r'@\w+',text,co)
            print(replac)
            verified=re.sub(r'VERIFIED|verified|Verified',"",replac)
            print(verified)
            with open("link"+str(i)+"comments.txt","a+",encoding='utf-8') as Comments:
                Comments.write(verified+'\n')
                sleep(randint(4,7))
                Num +=1
        else:
            break

#method to read links
def Linkfile(i,driver,name):
    global limit
    v=0
    with open(File) as Links:
       Link = Links.readlines()[i]
       print (Link)
       driver.get(Link)
       sleep(4)
       #sprint driver.find_element_by_class_name('_6lAjh')
       print ('Loading Comments...')
       while True:
            
            try: 
                if limit>12 and limit<24:
                    driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                    sleep(3)
                    break
                elif limit>24 and limit<36:
                    driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                    sleep(3)
                    v+=1
                    if v==3:
                        break
                elif limit>36 and limit<48:
                   driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                   sleep(3)
                   v+=1
                   if v==4:
                       break
                elif limit>36 and limit<48:
                   driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                   sleep(3)
                   v+=1
                   if v==5:
                       break
                elif limit>48 and limit<60:
                   driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                   sleep(3)
                   v+=1
                   if v==6:
                       break
                elif limit>60 and limit<72:
                   driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                   sleep(3)
                   v+=1
                   if v==7:
                       break

                elif limit>72 and limit<84:
                   driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                   sleep(3)
                   v+=1
                   if v==8:
                       break

                elif limit>84 and limit<96:
                   driver.find_element_by_css_selector('.glyphsSpriteCircle_add__outline__24__grey_9.u-__7').click()
                   sleep(3)
                   v+=1
                   if v==9:
                       break
                else: 
                    break

            except:
                break
       comments(driver,i,name); 
       sleep(4)
       driver.delete_all_cookies()
       

def main():
    global name
    global nooflinks 
    profile = webdriver.FirefoxProfile()
    profile.set_preference("browser.cache.disk.enable", False)
    profile.set_preference("browser.cache.memory.enable", False)
    profile.set_preference("browser.cache.offline.enable", False)
    profile.set_preference("network.http.use-cache", False) 
    driver =webdriver.Firefox(profile)
    try:
        sleep(2)
        driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
        sleep(3)
        driver.find_element_by_name('username').send_keys(Username)
        driver.find_element_by_name('password').send_keys(Password)
        driver.find_element_by_name('password').send_keys(Keys.RETURN)
        sleep(4)
    except:
        pass
    for i in range(0,nooflinks):
        Linkfile(i,driver,name);
                 
if __name__ == "__main__":
    main()

