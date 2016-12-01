from bs4 import BeautifulSoup as bs
import requests
import re

class susiso_parser(object):
    def __init__(self):
        self.susiso_url = 'http://smartsw.ssu.ac.kr'
        self.url_base = 'http://smartsw.ssu.ac.kr/rb/?c=2/38'

    def refresh_notificationt(self):
        self.r = requests.get(self.url_base)
        self.soup = bs(self.r.text, 'html.parser')
        
        self.noti_list = [noti.text for noti in self.soup.find('div', {'id' : 'bbslist'}).find_all('span', {'class' : 'subject'})]
        self.date_list = [re.search("[0-9]{4}.[0-9]{2}.[0-9]{2}",tr.text).group() for tr in self.soup.find('div', {'id' : 'bbslist'}).find_all('div', {'class' : 'info'})]

        self.link_list = [tr.get('onclick') for tr in self.soup.find('div', {'id' : 'bbslist'}).find_all('div', {'class': 'list notice'})]

        #self.visit_count_list = [tr.find_all('td')[self.visit_count].text for tr in self.soup.tbody.find_all("tr")]

        self.my_tb = zip(self.noti_list, self.date_list, self.link_list)

    def get_notification(self):
        self.ret = ''
        self.refresh_notificationt()
        
        for noti, date, link in self.my_tb:
            self.ret += '<a href={link}>{notification}</a> \n스시소 공지:{date}\n'.format(\
                    link = '{head_url}{tail_url}'.format(head_url=self.susiso_url,tail_url=re.search('[/][r][b].*[0-9]{4}', link).group()) ,
                    notification = noti,
                    date = date)
            self.ret.replace('\t', '')
        return self.ret

