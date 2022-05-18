from bs4 import BeautifulSoup 

with open('home.html', 'r') as html_file:
    content=html_file.read()

    soup=BeautifulSoup(content, 'lxml')

    ## this finds specifics tags using the beautiful soup library
    ##find_all finds all the element with h5 tags b
    # course_html_tags =soup.find_all('h5')
    # for course in course_html_tags:
    #     print(course.text)

    course_cards=soup.find_all('div', )
   

       