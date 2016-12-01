from bs4 import BeautifulSoup as bs
import requests
import re

class ssu_parser(object):
    def __init__(self):
        self.url_base = 'http://www.ssu.ac.kr/web/kor/plaza_d_01'
        self.noti_outline = 1
        self.date = 4
        self.visit_count = 5

    def refresh_notificationt(self):
        self.r = requests.get(self.url_base)
        self.soup = bs(self.r.text, 'html.parser')

        self.noti_list = [noti.text for noti in self.soup.find('div', {'id' : 'bbslist'}).find_all('span', {'class' : 'subject'})]

        self.date_list = [re.search("[0-9]{4}.[0-9]{2}.[0-9]{2}",tr.text).group() for tr in
                self.soup.find('div', {'id' : 'bbslist'}).find_all('div', {'class' : 'info'})]
        #self.visit_count_list = [tr.find_all('td')[self.visit_count].text for tr in self.soup.tbody.find_all("tr")]
        self.link = [tr.get('href') for tr in soup.tbody.find_all('a', href=True)]

        self.my_tb = zip(self.dept_list, self.noti_list, self.date_list, self.link)

    def get_notification(self):
        self.ret = ''
        refresh_notificationt()
        
        for dept, noti, date, link in self.my_tb:
            ret += '[{department}] <a href={link}>{notification}</a> \n스시소 공지:{date}\n'.format(\
                    department = dept,
                    notification = noti,
                    date = date,
                    link = link)
            ret.replace('\t', '')
        return ret

