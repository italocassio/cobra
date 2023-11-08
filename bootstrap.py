#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# italovisk.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :
from selenium.webdriver.remote.webdriver import By
import undetected_chromedriver as uc
import os
from time import sleep

options = uc.ChromeOptions()

options.add_argument("--headless=new")
options.accept_insecure_certs = True
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--ignore_ssl")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1280,720")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--ignore-certificate-errors")

# driver = uc.Chrome(options=options)
#sudo zypper up google-chrome-stable 

try:
    driver = uc.Chrome(options=options)
except Exception as ex:
    chrome_driver_path = "/usr/bin/google-chrome"
    driver = uc.Chrome(options=options, browser_executable_path=chrome_driver_path)

sleep(0.5)
driver.get("http://www.comprasnet.gov.br/seguro/loginPortalFornecedor.asp")
sleep(0.5)
# btn_click = driver.find_element(By.CSS_SELECTOR, "button.br-button:nth-child(2)")
# btn_click.click()
# acc_txt = driver.find_element(By.ID, "accountId")
# acc_txt.send_keys("123")
# btn_click = driver.find_element(By.CSS_SELECTOR, "#login-button-panel > button")
# btn_click.click()

os.popen("cp ~/.local/share/undetected_chromedriver/undetected_chromedriver .")

sleep(0.5)
print("ok")
