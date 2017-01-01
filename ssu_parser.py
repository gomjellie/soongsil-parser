from bs4 import BeautifulSoup as bs
import requests
import re

class ssu_parser(object):
    def __init__(self):
        self.url_base = 'http://www.ssu.ac.kr/web/kor/plaza_d_01'
        self.noti_outline = 1
        self.department = 3
        self.date = 4
        self.visit_count = 5

    def refresh_notification(self):
        self.r = requests.get(self.url_base)
        self.soup = bs(self.r.text, 'html.parser')

        self.link = [tr.get('href') for tr in self.soup.tbody.find_all('a', href=True)]
        self.noti_list = [tr.find_all('td')[self.noti_outline].text for tr in self.soup.tbody.find_all("tr")]
        self.dept_list = [tr.find_all('td')[self.department].text for tr in self.soup.tbody.find_all("tr")]
        self.date_list = [tr.find_all('td')[self.date].text for tr in self.soup.tbody.find_all("tr")]
        #self.visit_count_list = [tr.find_all('td')[self.visit_count].text for tr in self.soup.tbody.find_all("tr")]

        self.my_tb = zip(self.dept_list, self.noti_list, self.date_list, self.link)

    def get_notification(self):
        self.ret = ''
        self.refresh_notification()

        for dept, noti, date, link in self.my_tb:
            self.ret += '[{department}] <a href={link}>{notification}</a> \n숭실대 공지:{date}\n'.format(
                department = dept.replace('\t', ''),
                notification = noti.replace('\t', ''),
                date = date,
                link = link)
            return self.ret

