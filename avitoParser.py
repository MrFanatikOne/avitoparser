# coding: utf8

import time
import random
import csv
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from builtins import input


class avitoParser():
    driver = ''
    login = ''
    password = ''
    name_of_item = ''
    count_items = 0
    city = ''


    def initData(self):
        opts = Options()
        opts.add_argument("user-agent=Mozilla/5.0 (Linux; Android 10; SM-N960U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.96 Mobile Safari/537.36 Instagram 145.0.0.32.119 Android (29/10; 480dpi; 1080x2076; samsung; SM-N960U; crownqltesq; qcom; en_US; 219308759)")
        opts.set_headless(True)
        self.driver = webdriver.Chrome(chrome_options=opts)
        self.driver.set_window_size(356, 900)
        self.inputData()

    def inputData(self):
        file = open('login.txt', mode='r')
        self.login = file.readline()
        self.password = file.readline()
        print('Введите поисковый запрос на авито:')
        self.name_of_item = input()
        print('Введите количесто обрабатываемых запросов:')
        self.count_items = int(input())
        print('Введите город в котором производится поиск(введите * для поиска по России)')
        self.city = input()
        print('Ждите выполнения программы. Рузльтат будет записан в файл {} {} {}.csv. Файл открывается программой excel.'.format(self.name_of_item, self.city, self.count_items))

    def findItems(self):
        if self.city == '*':
            self.city = 'Россия'
        file = open('{} {} {}.csv'.format(self.name_of_item, self.city, self.count_items), mode='w', encoding='utf-16')
        file_csv = csv.writer(file, delimiter="\t", lineterminator="\r")
        self.driver.get("http://www.avito.ru")
        time.sleep(1)
        close_btn = self.driver.find_element(By.ID, "splash-banner-click-negative")
        close_btn.click()
        time.sleep(1)
        search_menu_bar = self.driver.find_element_by_xpath('//div[@data-marker="search-bar/menu"]').find_element_by_tag_name('i')
        search_menu_bar.click()
        time.sleep(random.randint(1, 3))
        loging_bar = self.driver.find_element_by_xpath('//div[@data-marker="menu/content"]').find_element_by_tag_name('a')
        loging_bar.click()
        time.sleep(random.randint(1, 3))
        loging_btn = self.driver.find_element_by_xpath('//div[@data-marker="login-button"]')
        loging_btn.click()
        time.sleep(random.randint(1, 3))
        input_login = self.driver.find_element_by_xpath('//input[@data-marker="login"]')
        input_login.click()
        input_login.clear()
        input_login.send_keys(self.login)
        input_password = self.driver.find_element_by_xpath('//input[@data-marker="password"]')
        input_password.click()
        input_password.clear()
        input_password.send_keys(self.password + '\n')
        time.sleep(random.randint(2, 5))
        try:
            menu_bar = self.driver.find_element_by_xpath('//div[@data-marker="settings/top-bar/back"]')
            menu_bar.click()
        except:
            print('Введите код с смс сообщения для аккаунта {}'.format(self.login))
            time.sleep(1)
            sms_text_test = input()
            input_field = self.driver.find_element(By.TAG_NAME, "input")
            input_field.send_keys(sms_text_test, +'\n')
            menu_bar = self.driver.find_element_by_xpath('//div[@data-marker="settings/top-bar/back"]')
            menu_bar.click()
        time.sleep(1)
        menu_search = self.driver.find_element_by_xpath('//a[@data-marker="menu/search"]')
        menu_search.click()
        time.sleep(random.randint(1, 3))
        try:
            btn_cancel = self.driver.find_element_by_xpath('//button[@data-marker="splash-banner/cancel-button"]')
            btn_cancel.click()
        except:
            pass
        time.sleep(random.randint(1, 3))
        input_field = self.driver.find_element_by_tag_name('input')
        input_field.click()
        input_field.clear()
        input_field.send_keys(self.name_of_item + '\n')
        time.sleep(random.randint(2, 4))
        option_bar = self.driver.find_element_by_xpath('//div[@data-marker="search-bar/filter"]')
        option_bar.click()
        time.sleep(random.randint(2, 4))
        choose_location = self.driver.find_element_by_xpath('//div[@data-marker="location-chooser"]')
        choose_location.click()
        time.sleep(random.randint(1, 2))
        field_cities = self.driver.find_element_by_xpath('//input[@data-marker="region-search-bar/search"]')
        field_cities.send_keys(self.city + '\n')
        time.sleep(random.randint(1, 2))
        cities_in_search = self.driver.find_element_by_xpath('//div[@data-marker="region-list/list"]').find_element(By.TAG_NAME, 'div')
        cities_in_search.click()
        time.sleep(random.randint(1, 3))
        close_btn = self.driver.find_element_by_xpath('//div[@data-marker="search-form"]').find_element(By.TAG_NAME, 'i')
        close_btn.click()
        time.sleep(random.randint(1, 3))
        url = self.driver.current_url
        time.sleep(random.randint(3, 6))
        elements = self.driver.find_elements_by_xpath('//a[@data-marker="item/link"]')
        i = 0
        mass_to_write = ['Ссылка', 'Адрес', 'Имя', 'Номер']
        while i < self.count_items:
            file_csv.writerow(mass_to_write)
            mass_to_write = []
            try:
                elements[i].click()
            except:
                return
            time.sleep(random.randint(1, 3))
            url_item = self.driver.current_url
            mass_to_write.append(url_item)
            try:
                loc = self.driver.find_element_by_xpath('//span[@data-marker="delivery/location"]')
                mass_to_write.append(loc.text.replace('\n', ' '))
            except:
                mass_to_write.append('none')
                pass
            try:
                name = self.driver.find_element_by_xpath('//span[@data-marker="seller-info/name"]')
                mass_to_write.append(name.text.replace('\n', ' '))
            except:
                mass_to_write.append('none')
                pass
            try:
                time.sleep(random.randint(1, 3))
                btn_call = self.driver.find_element_by_partial_link_text('Позвонить')
                btn_call.click()
                time.sleep(random.randint(1, 3))
                phone = self.driver.find_element_by_xpath('//span[@data-marker="phone-popup/phone-number"]')
                mass_to_write.append(phone.text.replace('\n', ' '))
            except:
                mass_to_write.append('none')
                pass
            self.driver.get(url)
            elements = self.driver.find_elements_by_xpath('//a[@data-marker="item/link"]')
            count_of_items = len(elements)
            while count_of_items < self.count_items and i > count_of_items - 10:
                self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                print(i)
                print(count_of_items)
                time.sleep(random.randint(1, 3))
                elements = self.driver.find_elements_by_xpath('//a[@data-marker="item/link"]')
                count_of_items = len(elements)
                try:
                    get_new_elements = self.driver.find_elements_by_partial_link_text('ЗАГРУЗИТЬ ЕЩЕ')
                    get_new_elements.click()
                except:
                    pass
            self.driver.execute_script("window.scrollTo(0,-1 * document.body.scrollHeight)")
            time.sleep(random.randint(1, 3))

            i += 1
            time.sleep(random.randint(2, 5))
        file_csv.writerow(mass_to_write)
        file.close()
        self.driver.quit()

