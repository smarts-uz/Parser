import bs4
from bs4 import BeautifulSoup
import os
import urllib.request

fname = r"mhtml_lists\messages.html"

def get_html(file_path):
    HtmlFile = open(file_path, 'r', encoding='utf-8')
    source_code = HtmlFile.read()
    soup = BeautifulSoup(source_code, 'html.parser')
    return soup

def get_info(html):
    page_body = html.find('div', class_='history') #class history
    messages_1 = page_body.find_all('div', class_='message default clearfix') #user's message
    messages_2 = page_body.find_all('div', class_='message default clearfix joined') #binded user's message
    list_test = []
    
    for i in [messages_1, messages_2]:
        body = i.find_all('div', class_='body')
        try:
            messages_3 = messages_2.find('div', class_='reply_to details') #binded
            messages_4 = messages_2.find('div', class_="media_wrap clearfix") #user's media
            messages_5 = messages_2.find('div', class_="text") #in that case this is link
            messages_6 = messages_4.find('div', class_="media clearfix pull_left block_link media_file")
            text = find('div', class_="text").get_text()
            list_test.append(text)
            with open('test.txt', 'a', encoding='UTF-8') as file:
                file.write(text)
            print(text)
        except:
            pass

    print(list_test)

main_html = get_html(fname)
result = get_info(main_html)
print(result)
