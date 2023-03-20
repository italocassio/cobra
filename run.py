#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# italovisk.py
# @Author : Gustavo (gustavo@gmf-tech.com)
# @Link   :
from selenium.webdriver.remote.webdriver import By
import undetected_chromedriver as uc
options = uc.ChromeOptions()
# options.headless = True
# options.add_argument("--headless")
# options.add_argument("--start-maximized")
# options.add_argument("--start-fullscreen")
# options.add_argument("--single-process")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("disable-infobars")
# options.add_argument("ignore-certificate-errors")
options.accept_insecure_certs = True
options.add_argument("--ignore_ssl")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--ignore-certificate-errors")

#driver = uc.Chrome(options=options)
 
#chrome_driver_path = "/home/italo/Documents/pocs/cobra/chromedriver"
chrome_driver_path ="/usr/bin/google-chrome-stable"
driver = uc.Chrome (version_main=111, options=options, browser_executable_path=chrome_driver_path)

driver.get("http://www.comprasnet.gov.br/seguro/loginPortalFornecedor.asp")
btn_click = driver.find_element(By.CSS_SELECTOR, "button.br-button:nth-child(2)")
btn_click.click()
acc_txt = driver.find_element(By.ID, "accountId")
acc_txt.send_keys("123")
btn_click = driver.find_element(By.CSS_SELECTOR, "#login-button-panel > button")
btn_click.click()
passwd_txt = driver.find_element(By.ID, "password")
passwd_txt.send_keys("123")
btn_click = driver.find_element(By.CSS_SELECTOR, "#submit-button")
btn_click.click()
print("ok")
