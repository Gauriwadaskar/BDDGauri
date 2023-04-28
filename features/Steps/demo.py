from behave import *
from selenium import webdriver
@given(u'open CE broswer')
def Openbroswer(context):
    context.driver =webdriver.Chrome(executable_path="E:\gauri python\\automation\seleniumproj\chromedriver_win32\chromedriver.exe")
@When (u'Enter url')
def urlEnter(Context):
    context.driver.get('https://demo.guru99.com/v3/')
