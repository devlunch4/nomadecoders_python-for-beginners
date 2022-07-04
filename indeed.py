import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://www.indeed.com/jobs?q=python&limit={LIMIT}"


def get_last_page():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "pagination"})

    links = pagination.find_all("a")
    pages = []
    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]
    return max_page


def extract_jobs(last_page):
    jobs = []
    # for page in range(last_page):
    result = requests.get(f"{URL}&start={0*LIMIT}")
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("td", {"class": "resultContent"})
    print("#")
    for result in results:
        # print(result.find("a").find({"span": "title"}).string)
        # print(result.find("h2", {"class": "jobTitle"}).text)
        title = result.find("h2", {"class": "jobTitle"}).text
        company = result.find("span", {"class":"companyName"}).text
        print(title)
        print(company)
        print()
        jobs.append(title)
    return jobs



def get_jobs():
  last_page = get_last_page()
  jobs = extract_jobs(last_page)
  return jobs