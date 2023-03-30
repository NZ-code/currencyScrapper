from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# data handling
import json
import pandas as pd
from time import sleep
from consts import *

# create driver with given options
options = Options()
driver = webdriver.Chrome(path, options=options)

# open website
driver.get(web)
driver.maximize_window()


base_currency_input =driver.find_element_by_xpath('//input[contains(@id,"baseCurrency")]')
quote_currency_input =driver.find_element_by_xpath('//input[contains(@id,"quoteCurrency")]')

def clear_input(input):
    """ Select whole input field and clear data """
    input.send_keys(Keys.CONTROL + "a")
    input.send_keys(Keys.DELETE)


def clear_and_send_keys(input, keys):
    """ Calling clear function + send keys to input"""
    clear_input(input)
    input.send_keys(str(keys))
def set_base_currency(c1):
    clear_and_send_keys(base_currency_input, c1)
    base_currency_input.send_keys(Keys.ARROW_DOWN)
    base_currency_input.send_keys(Keys.ENTER)
def set_quote_currency(c2):
    clear_and_send_keys(quote_currency_input, c2)
    quote_currency_input.send_keys(Keys.ARROW_DOWN)
    quote_currency_input.send_keys(Keys.ENTER)



def get_currency_k(c1,c2):

    sleep(3)
    k = driver.find_elements_by_xpath('//input[contains(@name, "numberformat")]')[1].get_attribute("value")
    print(k)
    return k

def get_all_currency_codes():
    code = []
    df = pd.read_csv('input/abrv.csv')
    return df.AlphabeticCode.values.flatten().tolist()


def get_all_exchanges(quote_currency_code):

    set_quote_currency(quote_currency_code)
    exchanges = {}
    base_codes = []
    quote_codes = []
    ks = []
    codes = get_all_currency_codes()
    for code in codes:
        set_base_currency(code)
        k = get_currency_k(code, quote_currency_code)
        base_codes.append(code)
        quote_codes.append(quote_currency_code)
        ks.append(k)
    exchanges['base'] = base_codes
    exchanges['quote'] = quote_codes
    exchanges['k'] = ks
    return exchanges

def save_exchanges_to_csv(exchanges):
    df = pd.DataFrame.from_dict(exchanges)
    df.to_csv("output/exchanges.csv")