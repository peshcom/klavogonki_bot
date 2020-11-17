#! /usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

import os


import time


url = "http://klavogonki.ru/g/?gmid=*******"

options = webdriver.FirefoxOptions()
options.set_preference('dom.webdriver.enabled', False)
options.set_preference('dom.webnotifications.enabled', False)
options.set_preference('media.volume_scale', '0.0')

driver = webdriver.Firefox(executable_path=os.path.abspath(".") + '/geckodriver', options=options, service_log_path="geckodriver.log")

# Временой интервал ожидания
# Если в течении этого времени элемент НЕ найдется, то упадем с ошибкой
driver.implicitly_wait(20) # seconds

# Переходим на страницу
driver.get(url)

def write_text(text):
	text = text.replace('c', 'с') # Замена на русскую С
	text = text.replace('o', 'о') # Замена на русскую о
	input_area = driver.find_element_by_id("inputtext")
	# if driver.find_element_by_class_name("afterfocus").text == '.':
	# 	input_area.send_keys(text + ".")
	# else:
	input_area.send_keys(text + " ")


def get_text():
	a = driver.find_element_by_class_name("highlight")
	return a.text


if __name__ == '__main__':
	print("Жду начала игры")
	input("Нажми enter")
	while 1:
		write_text(get_text())
		# time.sleep(0.01)
