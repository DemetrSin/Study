import os.path

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

from links import job_links
from send_mail import send_email


class BSParser:
    def __init__(self, url, http=None):
        self.url = url
        self.http = http

    @staticmethod
    def get_random_user_agent():
        user_agent = UserAgent()
        return user_agent.random

    def if_not_200(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        html_content = driver.page_source
        driver.quit()
        return html_content

    def fetch_job_listings(self):
        headers = {
            "User-Agent": self.get_random_user_agent()}
        response = requests.get(self.url, headers=headers)
        if response.status_code == 200:
            return response.content
        else:
            html_content = self.if_not_200()
            return html_content

    def parse_job_listings(self, html_content):
        words = ['python', 'django', 'fastapi']
        job_info = {}
        soup = BeautifulSoup(html_content, 'html.parser')
        h2_els = soup.find_all('a')
        for el in h2_els:
            for word in words:
                if word in el.text.lower():
                    href = el.get('href')

                    if self.http:
                        job_info[' '.join(el.text.split())] = self.http + href
                    else:
                        job_info[' '.join(el.text.split())] = href

        return job_info

    @staticmethod
    def filter_listings(job_listing):
        words = ['qa', 'test', 'full-stack', 'senior', 'aqa', 'salary', 'ml']
        key_for_delete = []
        for k in job_listing:
            if set(k.lower().split()).intersection(words):
                key_for_delete.append(k)
        for key in key_for_delete:
            del job_listing[key]

        return job_listing

    def main(self):
        html_content = self.fetch_job_listings()
        if html_content:
            job_listings = self.parse_job_listings(html_content)
            filtered_listings = self.filter_listings(job_listings)
            with (open('data.txt', 'r', encoding='utf-8') as file_read,
                  open('data2.txt', 'a', encoding='utf-8') as file_append):
                data = file_read.read()
                for job, href in filtered_listings.items():
                    if str(href) not in data:
                        file_append.write(job + ' : ' + str(href) + '\n'*2)


if __name__ == '__main__':
    if os.path.exists('data2.txt'):
        os.remove('data2.txt')

    for x in job_links:
        instance = BSParser(*x)
        instance.main()

    send_email()

















