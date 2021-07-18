from bs4 import BeautifulSoup
import requests
#import lxml
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title)
# #print(soup.prettify())
# #print(soup.a)
#
# # all the anchor tags
# all_anchor_tags = soup.find_all(name="a")
#
# # for tag in all_anchor_tags:
#     # print(tag.getText()) # print tag names
#     # print(tag.get("href")) # print all the links
#
#
# heading = soup.find(name="h1", id="name")
# #print(heading)
#
# section_heading = soup.find(name="h3", class_="heading") #class_ because class is a reserved word
# #print(section_heading.get("class"))
#
# # give first matching item
# company_url = soup.select_one(selector="p a")
# #print(company_url)
#
# name = soup.select_one(selector="#name")
# #print(name)
#
# headings = soup.select(".heading")
# print(headings)
#
# response = requests.get("https://news.ycombinator.com")
# yc_webpage = response.text
#
# soup = BeautifulSoup(yc_webpage, "html.parser")
# # print(soup.title)
# article_texts = []
# article_links = []
# article_tag = soup.find_all(name="a", class_="storylink")
# for articles in article_tag:
#     article_text = articles.getText()
#     article_texts.append(article_text)
#     article_link = articles.get("href")
#     article_links.append(article_link)
# print(article_texts)
# print(article_links)
#
#
# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
# print(article_upvotes)
#
# highest = article_upvotes.index(max(article_upvotes))
# # print(highest)
#
# print(article_texts[highest])
# print(article_links[highest])


# print(article_text, article_link, article_score)

