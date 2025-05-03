# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.proxy import *
from selenium.webdriver.common.action_chains import ActionChains
import time
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox, FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import ElementNotVisibleException,NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from random import *
from selenium.webdriver.firefox.options import Options
options=Options()
options.headless=False


fp = FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png,")
fp.set_preference('startup.homepage_welcome_url', 'about:blank')
fp.set_preference("browser.startup.page", "0")
fp.set_preference("browser.startup.homepage", "about:blank")
fp.set_preference("browser.safebrowsing.malware.enabled", "false")
fp.set_preference("startup.homepage_welcome_url.additional", "about:blank")
fp.update_preferences()

def log_exception(e):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print("[ + ]  Line no :{0} Exception {1}".format(exc_traceback.tb_lineno,e))


def get_driver(proxy_host,proxy_port):
    PROXY = '{0}:{1}'.format(proxy_host,proxy_port)
    myproxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': PROXY,
        'ftpProxy': PROXY,
        'sslProxy': PROXY
        # 'noProxy': ','.join(excluded_from_proxy)  # set this value as desired
        })
    # driver = Firefox(firefox_binary=FirefoxBinary('/home/we45/Downloads/firefox-46.0.linux-x86_64.sdk/firefox-sdk/bin/firefox'), firefox_profile=fp,proxy=myproxy)    
    driver = Firefox(fp,options=options)
    # driver = Firefox(fp,proxy=myproxy)
    print("Initialized firefox driver")
    driver.maximize_window()    
    driver.implicitly_wait(120)
    return driver

url = "https://staging.learning.appsecengineer.com/"

def mailid():
    x = randint(0,999)
    # domain = "@we45.com"
    letter = 'test_we45{0}'.format(x)
    return letter

mail = mailid()
print(mail)
info = mail+'@we45.com'
print(info)

email_login='madhu.kumar@we45.com'
email_password= ' '

def Login(driver,target):
    try:
        print("Login")
        # driver.get('{0}/login.htm'.format(target))
        driver.get('{0}'.format(target))
        driver.implicitly_wait(20)
        time.sleep(8)
        

        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/form/div/label/div/div[1]/div/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/form/div/label/div/div[1]/div/input').send_keys(email_login)
        driver.implicitly_wait(20)
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/form/a/span[2]').click()
        driver.implicitly_wait(20)
        time.sleep(3)
        driver.find_element_by_id("identifierId").clear()
        driver.implicitly_wait(20)
        driver.find_element_by_id("identifierId").send_keys(email_login)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span').click()
        driver.implicitly_wait(20)
        time.sleep(3)
        driver.find_element_by_name('Passwd').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_name('Passwd').send_keys(email_password)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[1]/div/div/button/span').click()
        driver.implicitly_wait(20)
        time.sleep(15)
        print("appsecengineer dashboard page")
        dashboard= driver.current_url
        print(dashboard)
    except BaseException as e:
        log_exception(e)


def dashboard(driver,target):
    try:
        driver.get('{0}portal/dashboard'.format(target))
        #Explore Pages
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section[1]/div[1]/div/div[1]/div/div/div/div[2]/div/div[3]/button/span[2]').clear()
        driver.implicitly_wait(20)
        time.sleep(20)
        print(driver.current_url)
        #See ALL
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section[1]/div[2]/div/div[2]/button/span[2]').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        #Certificates
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/main/div/div[3]/div/div/div/div[1]/div/div[2]/div[2]/div').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        print('certificates')
        #Badges
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/main/div/div[3]/div/div/div/div[1]/div/div[3]/div[2]/div').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        print('Badges')
        driver.get('{0}portal/profile/activity'.format(target))
        driver.implicitly_wait(20)
        time.sleep(10)
        print('Activity')
        driver.get('{0}portal/courses'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        courses= driver.current_url
        print(courses)
        print('courses')
    except BaseException as e:
        log_exception(e)


def Courses(driver,target):
    try:
        driver.get('{0}portal/courses'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        courses= driver.current_url
        print(courses)
        print('courses')
    except BaseException as e:
        log_exception(e)

def journeys(driver,target):
    try:
        driver.get('{0}portal/journeys'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        journeys= driver.current_url
        print(journeys)
        print('journeys')
    except BaseException as e:
        log_exception(e)

def live_events(driver,target):
    try:
        driver.get('{0}portal/live-courses'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        live_courses= driver.current_url
        print(live_courses)
        print('live_courses')
    except BaseException as e:
        log_exception(e)

def Challenges(driver,target):
    try:
        driver.get('{0}portal/challenges'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        Challenges= driver.current_url
        print(Challenges)
        print('Challenges')
    except BaseException as e:
        log_exception(e)

def Assignments(driver,target):
    try:
        driver.get('{0}portal/company/assignments'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        assignments= driver.current_url
        print(assignments)
        print('assignments')
    except BaseException as e:
        log_exception(e)

def Playgrounds(driver,target):
    try:
        driver.get('{0}portal/playgrounds'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        playgrounds= driver.current_url
        print(playgrounds)
        print('playgrounds')
    except BaseException as e:
        log_exception(e)

def Running_Labs(driver,target):
    try:
        driver.get('{0}portal/running-labs'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        Running_Labs= driver.current_url
        print(Running_Labs)
        print('Running Labs')
    except BaseException as e:
        log_exception(e)

def Admin_user(driver,target):
    try:
        driver.get('{0}portal/company/company-users'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        user= driver.current_url
        print(user)
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div/div[1]/button/span[2]/span').click()
            driver.implicitly_wait(20)
            time.sleep(5)
        except BaseException as e:
            pass
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[2]/div/div/div[1]/div/div[1]/button/span[2]/span').click()
            driver.implicitly_wait(20)
            time.sleep(10)
        except BaseException as e:
            pass
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div[2]/div/div').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        #First name
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[1]/div/label/div/div[1]/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[1]/div/label/div/div[1]/div[1]/input').send_keys('Test')
        driver.implicitly_wait(20)
        time.sleep(5)
        #Last name
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[2]/div/label/div/div[1]/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[2]/div/label/div/div[1]/div[1]/input').send_keys(x)
        driver.implicitly_wait(20)
        time.sleep(5)
        #mailid
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[3]/div/label/div/div[1]/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[3]/div/label/div/div[1]/div[1]/input').send_keys(info)
        driver.implicitly_wait(20)
        time.sleep(5)
        #drop down
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[4]/div/label/div/div[1]/div[2]/i').click()
        driver.implicitly_wait(20)
        time.sleep(2)
        #Other
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[4]/div/label/div/div[1]/div[2]/i').send_keys(Keys.DOWN*4)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[4]/div/label/div/div[1]/div[2]/i').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(2)
        #DOB
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[5]/div/div/label/div/div[1]/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[2]/div[1]/div[5]/div/div/label/div/div[1]/div[1]/input').send_keys('1993')
        driver.implicitly_wait(20)
        time.sleep(5)
        #Submit button
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/form/div[3]/button[2]').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        print('create user')
    except BaseException as e:
        log_exception(e)

def Admin_Teams(driver,target):
    try:
        driver.get('{0}portal/company/teams'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        #create Team
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div[3]/button/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        #Name
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div/div/div/div/div[1]/label/div/div[1]/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div/div/div/div/div[1]/label/div/div[1]/div[1]/input').send_keys(mail)
        driver.implicitly_wait(20)
        time.sleep(10)
        #Submit button
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div/div/div/div/div[2]/button/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        print('Team Created')      
    except BaseException as e:
        log_exception(e)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[2]/div/div[2]/label/div/div/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[2]/div/div[2]/label/div/div/div[1]/input').send_keys(mail)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[2]/div/div[2]/label/div/div/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(10)
        #Detailed view
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/div/table/tbody/tr[1]/td[3]/div/i').click()
        driver.implicitly_wait(20)
        time.sleep(5)
        #Add members Team
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div/div/div/table/tbody/tr[2]/td/div/div[2]/div[2]/button/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        #Add users
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div/div/div/label/div/div[1]/div[1]/div[1]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div/div/div/label/div/div[1]/div[1]/div[1]/input').send_keys(email_login)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div/div/div/label/div/div[1]/div[1]/div[1]/input').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[1]/div/div/div/label/div/div[1]/div[1]/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(20)
        #Save button
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/form/div[2]/button/span[2]').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        #Team reports
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[2]/div/div[1]/div/div[2]/div[2]/div').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        print('Team completed')
    except BaseException as e:
        log_exception(e)

def Admin_Build_challenge(driver,target):
    try:
        driver.get('{0}portal/custom-challenge'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        #choose language
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/label[1]/div/div[1]/div[1]/div[1]/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/label[1]/div/div[1]/div[1]/div[1]/input').send_keys('python')
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/label[1]/div/div[1]/div[1]/div[1]/input').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/label[1]/div/div[1]/div[1]/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #Framework
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[1]/div[1]/label/div/div[1]/div/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[1]/div[1]/label/div/div[1]/div/input').send_keys('Django')
        driver.implicitly_wait(20)
        time.sleep(5)
        #vulnerability
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[1]/div[2]/label/div/div[1]/div[1]/div[1]/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[1]/div[2]/label/div/div[1]/div[1]/div[1]/input').send_keys('SQL Injection')
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[1]/div[2]/label/div/div[1]/div[1]/div[1]/input').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[1]/div[2]/label/div/div[1]/div[1]/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #Difficulty level
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[1]/label/div/div/div[1]/div[1]/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[1]/label/div/div/div[1]/div[1]/input').send_keys('intermediate')
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[1]/label/div/div/div[1]/div[1]/input').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[1]/label/div/div/div[1]/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #Answer Type
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[2]/label/div/div/div[1]/div[1]/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[2]/label/div/div/div[1]/div[1]/input').send_keys('Code')
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[2]/label/div/div/div[1]/div[1]/input').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[2]/div[2]/label/div/div/div[1]/div[1]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #Score
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[3]/label/div/div[1]/div/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[1]/div/div[3]/label/div/div[1]/div/input').send_keys('40')
        driver.implicitly_wait(20)
        time.sleep(5)
        #SHow me challenge button
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/section/div[1]/form/div[2]/button').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        print('Build Challenge completed')      
    except BaseException as e:
        log_exception(e)

def Admin_Reports(driver,target):
    try:
        driver.get('{0}portal/company/reports'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)        
        print('Reports')      
    except BaseException as e:
        log_exception(e)

def Admin_tournaments(driver,target):
    try:
        driver.get('{0}portal/company/tournaments'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)    
        #Create Tournament
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/button/span[2]/span').click()    
        driver.implicitly_wait(20)
        time.sleep(10)
        #NAME
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[1]/label/div/div[1]/div/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[1]/label/div/div[1]/div/input').send_keys(mail)
        driver.implicitly_wait(20)
        time.sleep(4)
        #description
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[2]/label/div/div[1]/div[1]/textarea').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[2]/label/div/div[1]/div[1]/textarea').send_keys('this is the tournament description Textarea')
        driver.implicitly_wait(20)
        time.sleep(4)
        #Start date
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[3]/label/div/div[1]/div[2]/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[3]/div/div[22]/button/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(5)
        #END date
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[4]/label/div/div[1]/div[2]/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div/div[3]/div/div[25]/button/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(5)
        #Pass Percentage
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[5]/label/div/div[1]/div/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[5]/label/div/div[1]/div/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[5]/label/div/div[1]/div/input').send_keys('50')
        driver.implicitly_wait(20)
        time.sleep(5)
        #time in minutes
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[6]/label/div/div[1]/div/input').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[6]/label/div/div[1]/div/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[6]/label/div/div[1]/div/input').send_keys('40')
        driver.implicitly_wait(20)
        time.sleep(5)
        #select Teams
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').send_keys(info)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #select Users
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').send_keys(email_login)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[7]/label/div/div[1]/div[1]/div/div').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #Submit button
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div/div/div/form/div[10]/button[2]/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        print('Tournaments')      
    except BaseException as e:
        log_exception(e)
    try:
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[2]/div[2]/div/div/div/button[1]/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        #Learning Paths
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/label/div/div/div[2]/i').click()
        driver.implicitly_wait(20)
        time.sleep(4)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/label/div/div/div[2]/i').send_keys(Keys.DOWN*9)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/label/div/div/div[2]/i').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        #Challenges
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/form/div[1]/label/div/div[1]/div[2]/i').click()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/form/div[1]/label/div/div[1]/div[2]/i').send_keys(Keys.DOWN)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/form/div[1]/label/div/div[1]/div[2]/i').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(5)
        # #Score
        # driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/form/div[1]/label/div/div[1]/div[2]/i').click()
        # driver.implicitly_wait(20)
        # driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/form/div[1]/label/div/div[1]/div[2]/i').send_keys(Keys.DOWN)
        # driver.implicitly_wait(20)
        #ATtach 
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[2]/div/form/button/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(20)
        #Submit button
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[2]/div[2]/div/div/div/div[3]/button').click()
        driver.implicitly_wait(20)
        time.sleep(20)
    except BaseException as e:
        log_exception(e)
    try:
        driver.get('{0}portal/company/tournaments'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        #Search Name
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div[1]/div/label/div/div/div[2]/input').clear()
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div[1]/div/label/div/div/div[2]/input').send_keys(mail)
        driver.implicitly_wait(20)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div[1]/div/label/div/div/div[2]/input').send_keys(Keys.ENTER)
        driver.implicitly_wait(20)
        time.sleep(10)
        #Finalize button
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[4]/div/div/div/table/tbody[2]/tr/td[5]/div/div[3]/div/div/span').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        #submit
        driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div/div[3]/div/button[2]/span[2]/span').click()
        driver.implicitly_wait(20)
        time.sleep(10)
        Print('Tournament created and finialized')
    except BaseException as e:
        log_exception(e)
    try:
        driver.get('{0}portal/company/assignments'.format(target))
        driver.implicitly_wait(20)
        time.sleep(20)
        print('assignments')
        #assignment
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/main/div[3]/div/div/div[1]/div[2]/div[1]/table/tbody/tr/td[1]').click()
        driver.implicitly_wait(20)
        time.sleep(20)
    except BaseException as e:
        log_exception(e)

class APPSec_walkthrough(object):

    def __init__(self, proxy_host = 'localhost', proxy_port = '8090', target = 'https://staging.learning.appsecengineer.com/'):
        self.proxy_host = proxy_host
        self.proxy_port = proxy_port
        self.target = target

    def run_script(self):
        try:
            driver = get_driver(self.proxy_host,self.proxy_port)
            driver.maximize_window()
            Login(driver,self.target)
            dashboard(driver,self.target)
            Courses(driver,self.target)
            journeys(driver,self.target)
            live_events(driver,self.target)
            Challenges(driver,self.target)
            Assignments(driver,self.target)
            Playgrounds(driver,self.target)
            Running_Labs(driver,self.target)
            Admin_user(driver,self.target)
            Admin_Teams(driver,self.target)
            Admin_Build_challenge(driver,self.target)
            Admin_Reports(driver,self.target)
            Admin_tournaments(driver,self.target)
        except BaseException as e:
            print("[ + ] Error !!!!!!!!!!!!",e)

s = APPSec_walkthrough()
s.run_script()


