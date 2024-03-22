import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_random_user_agent():
    user_agent = UserAgent()
    return user_agent.random


def fetch_job_listings():
    url = f"https://www.work.ua/en/jobs-junior+python+developer/"
    headers = {
        "User-Agent": get_random_user_agent()}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print("Failed to fetch job listings.")
        return None


def parse_job_listings(html_content):
    job_info = {}
    soup = BeautifulSoup(html_content, 'html.parser')
    h2_els = soup.find_all('a')
    for el in h2_els:
        if 'Python' in el.text:
            href = el.get('href')
            job_info[el.text.strip()] = 'https://www.work.ua' + href

    return job_info


def filter_listings(job_listing):
    words = ['QA', 'Test', 'Full-stack', 'Senior', 'AQA', 'salary']
    key_for_delete = []
    for k in job_listing:
        if set(k.split()).intersection(words):
            key_for_delete.append(k)
    for key in key_for_delete:
        del job_listing[key]

    return job_listing


def main():
    html_content = fetch_job_listings()
    if html_content:
        job_listings = parse_job_listings(html_content)
        filtered_listings = filter_listings(job_listings)
        for job, href in filtered_listings.items():
            print(job, href)


if __name__ == "__main__":
    main()
