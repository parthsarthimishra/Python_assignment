import mysql.connector
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import time
import json
#import my files 

import credentials
import connector 
import xpaths
# python_ass = mysql.connector.connect(
#      host="localhost",
#      user="python_user",
#      password=credentials.root_pass,
#      database="python_ass",
#      auth_plugin="mysql_native_password"
# )
#print("check-1")
class Person:
    #print("check-2")
    def __init__(self, name, city="Roorkee", work=None):
        self.name=name
        self.city=city
        if work is not None:
            self.work=work

    def show(self):
        print("My name is "+self.name+" and my current city is "+self.city)

    def upload(self, username):
        
        upload_command="UPDATE user SET name=%s,work=%s,city=%s WHERE username=%s"
        connector.python_ass.cursor().execute(upload_command , (str(self.name), json.dumps(self.work), str(self.city), username))
        connector.python_ass.commit()

def fwork(username, soup):
    work=[]
    for link in soup.find_all('div'):
        if link.string=="कार्य":
            break
    req_div=link.parent.parent.parent.parent.parent.contents[1]
    #multiple works possible (loop appending all in work[])
    for div in req_div.children:
        work.append(div.contents[0].contents[1].contents[0].contents[0].contents[0].string)
    print(work)
    return work


def fname(username, soup):
   return soup.find('h3').string #finds name in h3

    
def c_city(username, soup):

    for link in soup.find_all('div'):
        if link.string=="वर्तमान शहर":
            break
    city=link.parent.parent.contents[1].contents[0].contents[0].string   #grandparent div of वर्तमान शहर common b/w city name 
    print("check find_city")
    # print(city)
    return city 

def likes(username):

    driver = webdriver.Firefox() 
    driver.maximize_window()
    time.sleep(2)

    driver.get("https://m.facebook.com/"+username+"/about")
    time.sleep(2)
    driver.find_element(By.XPATH, xpaths.login_click).click()

    email = driver.find_element_by_id("m_login_email")
    password = driver.find_element_by_id("m_login_password")

    email.send_keys(credentials.my_email)
    password.send_keys(credentials.my_pass)

    password.send_keys(Keys.RETURN)
    time.sleep(15)

    SCROLL_PAUSE_TIME = 3

    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    time.sleep(2)

   
    
    driver.find_element(By.XPATH, xpaths.Likes_xpath).click()

    time.sleep(3)
    
    driver.find_element(By.XPATH, xpaths.All_likes_xpath).click()
    
    time.sleep(10)
    fav =[]
    
    for span in driver.find_elements(By.XPATH,xpaths.likes_1 ):
        fav.append(span.text)
    
    for span in driver.find_elements(By.XPATH, xpaths.likes_2):
        fav.append(span.text)

    print("Favourites / LIKES: ")
    print(fav)
    driver.quit()    



            
            #validate 
def check(result):
    for i in result:
        if(i[1] is not None):
            if(i[2] is not None):
                if(i[3] is not None):
                    return Person(name=i[1], city= i[3], work=i[2])
                else:
                    return Person(name=i[1], city= i[3])
            else:
                if(i[3] is not None):
                    return Person(name=i[1], work=i[2])
                else:
                    return Person(name=i[1])

        else:
            return None

def validate(func):
    def inner(username):
        mycursor = connector.python_ass.cursor()
        mycursor.execute("SELECT * FROM user where username=\'"+username+"\'")

        result = mycursor.fetchall()
        found=False
        #print("this is my result:")
        #print(myresult)
        for i in result:
            #print("this is i")
           # print(i)
            found=True

        if(found==False):
            raise ValueError('username not found')
        else:
            previous= check(result)
            if(previous is not None):
                previous.show()
            else:
                func(username)

        return "Validation end"

    return inner

@validate    
def scrap(username):
    #print("check-3")
    URL= "https://m.facebook.com/"+username+"/about"
    #print("check-6")
    req = requests.get(URL)
    #print("check-4")
    soup = BeautifulSoup(req.content, 'html.parser') 
    #print("check-5")
    name= fname(username, soup)
    city=c_city(username, soup)
    work= fwork(username, soup)
    likes(username)
    #print(work)
    #print(name)
    #print(city)
    person= Person(name, city, work)
    #print details
    person.show()
    person.upload(username)

#take input and start here    
username=input("Username to scrap: ")      
scrap(username)
       