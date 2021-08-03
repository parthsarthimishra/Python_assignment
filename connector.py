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


python_ass = mysql.connector.connect(
    host="localhost",
    user="python_user",
    password=credentials.root_pass,
    database="python_ass",
    auth_plugin="mysql_native_password"
)

test_python_ass = mysql.connector.connect(
    host="localhost",
    user="root",
    password=credentials.root_pass,
    database="fake_python_assignment",
    auth_plugin="mysql_native_password"
)