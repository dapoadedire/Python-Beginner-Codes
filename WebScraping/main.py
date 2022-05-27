from bs4 import BeautifulSoup

with open('index.html', 'r') as blog:
    content = blog.read()
    #print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify)

    # tags = soup.find('h2')
    # tags = soup.find_all('h2')
    # print(tags)
    # for tag in tags:
        # print(tag.text)
    tags = soup.find_all('div', class_="post-entry")
    # print(tags)
    for tag in tags:
        article_title = tag.h2.text
        article_body = tag.p.text
        print(article_title, article_body)
        # print(tag.h2)