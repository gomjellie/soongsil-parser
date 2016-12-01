from bs4 import BeautifulSoup as bs
import requests
import re

class susiso_parser(object):
    def __init__(self):
        self.url_base = 'http://smartsw.ssu.ac.kr/rb/?c=2/38'
        self.noti_outline = 1
        self.department = 3
        self.date = 4
        self.visit_count = 5

    def refresh_notificationt(self):
        self.r = requests.get(self.url_base)
        self.soup = bs(self.r.text, 'html.parser')

        self.noti_list = [tr.find_all('td')[self.noti_outline].text for tr in self.soup.tbody.find_all("tr")]
        self.dept_list = [tr.find_all('td')[self.department].text for tr in self.soup.tbody.find_all("tr")]
        self.date_list = [tr.find_all('td')[self.date].text for tr in self.soup.tbody.find_all("tr")]
        #self.visit_count_list = [tr.find_all('td')[self.visit_count].text for tr in self.soup.tbody.find_all("tr")]

        self.my_tb = zip(self.dept_list, self.noti_list, self.date_list)

    def get_notification(self):
        self.ret = ''
        refresh_notificationt()
        
        for dept, noti, date in self.my_tb:
            ret += '[{department}] {notification} \n스시소 공지:{date}\n'.format(\
                    department = dept,
                    notification = noti,
                    date = date)
            ret.replace('\t', '')
        return ret

