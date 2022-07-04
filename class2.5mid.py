import requests
from bs4 import BeautifulSoup
'''
#2.3 Extracting Indeed Pages (10:21)
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")
# print(indeed_result)
# print(indeed_result.text)

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})
pages = pagination.find_all("a")
# print(pages)

spans = []
for page in pages:
    # print(page.find("span"))
    spans.append(page.find("span").string)
# print(spans[0:-1])
spans = spans[0:-1]
print(spans)
################



#2.4 Extracting Indeed Pages part Two (07:34) START
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")
pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]
################
'''

#2.5 Requesting Each Page (10:29) START
indeed_result = requests.get("https://www.indeed.com/jobs?q=python&limit=50")

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")
# print(indeed_soup)

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")
pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]
print(max_page)

for n in range(max_page):
    print(f"start={n*50}")
################
