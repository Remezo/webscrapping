from bs4 import BeautifulSoup 
import requests


print("input some unfamiliar skilss separated by a space")
inp=input(">")
unfamilliar_skills=inp.split()




print("This might take a few seconds")
value=False

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

#Step 2
soup=BeautifulSoup(html_text, 'lxml')
jobs=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

for job in jobs:
    time=job.find('span', class_='sim-posted').text

    if 'few' in time:
        company_name=job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skills=job.find('span', class_='srp-skills').text.replace(' ', '')
        more_info=job.header.h2.a['href']

        for unfamiliar in unfamilliar_skills:
            if unfamiliar in skills:
                value=True
        
        if value==False:
            print(f"company _name: {company_name.strip()}")
            print(f"skills:{skills.strip()}")
            print(f"more_info:{more_info}")

            print('')
