# importing the necessary libraries
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import urllib.request

searchKey = ''

# Setting the necessary flags to improve the performance of the selenium crawler
options = Options()
prefs = {
    "profile.managed_default_content_settings.stylesheets": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument("--disable-extensions")
options.add_argument("--disable-notifications")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

# setting up the link
link = 'https://www.instagram.com'
# The page of which description i want to crawl make sure the acount is public
usernameToCrawl = 'food.lovers.nepal'
#User name and password of your account
username = 'username'
password = 'password'

#Getting the link
driver.get(link)

#Creating and array to store all the details
allDetails=[]

#Creating a function to sign in to instagram
def signIn(element):
    #Getting the username input block
    usernameBlock = element.find_element(By.NAME, 'username')
    #Getting the password input block
    passwordBlock = element.find_element(By.NAME, 'password')
    #Getting the submit button
    submit = element.find_element(By.TAG_NAME, 'button')
    #using send keys to add username and password in the dedicated block
    usernameBlock.send_keys(username)
    passwordBlock.send_keys(password)
    #Simulating button click
    submit.click()


    #Sleneium treats every instatnce as new so when we login to the instagram, instagram asks to save info
    # Identifying if that block is visible
    elementNew = None
    try:
        elementNew = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME,'button'))
        )
    except Exception as E:
        print(E)

    if(elementNew==None):
        time.sleep(10)

    #Creating the new link
    newlink = f'{link}/{usernameToCrawl}'
    driver.get(newlink)
    time.sleep(5)

    #Using scroll to get more posts this can be done in loop to get all posts
    driver.execute_script("window.scrollTo(0, 200)")
    print('Scrolled!')


    #Getting the link to all the posts, post description is only available in post details
    mainClass = driver.find_elements(By.CLASS_NAME,'x1lliihq')
    for singleClass in mainClass:
        print(singleClass.get_attribute('class'))
        print("Getting Post Link")
        #Getting the link of post
        xelement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@href, '/p/')]"))
        )

        postLink = xelement.get_attribute('href')

        #Opening the post details and getting description
        driver.get(postLink)
        time.sleep(5)
        details = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div/span/div/span').get_attribute('innerHTML')
        print(details)


        #My use case specially involved saving the description containing location // update as  per your need
        if('Location'.lower() in details.lower()):
            allDetails.append(details)




#Wating for login page to load
element = WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.ID, 'loginForm'))
)
signIn(element)

print(allDetails)

