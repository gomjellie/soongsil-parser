from bs4 import BeautifulSoup as bs
import requests
import re

class susiso_parser(object):
    def __init__(self):
        usl_base = 'http://www.ssu.ac.kr/web/kor/plaza_d_01'

    def refresh_notificationt(self):
        self.r = requests.get(url_base)
        self.soup = bs(r.text, 'html.parser')

        self.noti_list = [tr.find_all('td')[1].text for tr in self.soup.tbody.find_all("tr")]
        self.dept_list = [tr.find_all('td')[3].text for tr in self.soup.tbody.find_all("tr")]
        self.date_list = [tr.find_all('td')[4].text for tr in self.soup.tbody.find_all("tr")]

        self.my_tb = zip(noti_list, dept_list, date_list)

