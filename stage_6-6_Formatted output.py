import os
import argparse
import requests
import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
from colorama import Fore
from requests_html import HTMLSession


# write your code here

parser = argparse.ArgumentParser()
parser.add_argument("ingredient_1")
args = parser.parse_args()
dir = args.ingredient_1
dir_exists = os.access(dir, os.F_OK)
web_page = input()
history = list()
session = HTMLSession()
file_name = ""
r = ""
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/88.0.4324.182 Safari/537.36"



def check_web():
    global file_name
    global web_page
    global r
    if re.search(r'^https:[/]{2}.*\.[a-z]*$', web_page):
        #r = requests.get(web_page, headers={'User-Agent': user_agent})
        r = session.get(web_page)
        file_name = web_page.replace(re.search(r'https://', web_page).group(), "")
        file_name = file_name.replace(re.search(r'(\.[a-z]*)*$', file_name).group(), "")
        history.append(file_name)
        file_esist()
    elif re.search(r'\.[a-z]*$', web_page):
        #r = requests.get("https://" + web_page, headers={'User-Agent': user_agent})
        r = session.get("https://" + web_page)
        file_name = web_page.replace(re.search(r'(\.[a-z]*)*$', web_page).group(), "")
        history.append(file_name)
        file_esist()
    else:
        print("Invalid URL")


def dir_exist(dir, dir_exists):
    if not dir_exists:
        # create the dir
        os.makedirs(dir)


def check():
    global web_page
    global file_name
    while web_page != "exit":

        if web_page == "exit":
            break
        elif web_page == "back":
            if history:
                file_name = history.pop()
                file_esist()
        else:
            check_web()

        web_page = input()


def file_esist():
    global r
    soup = BeautifulSoup(r.content, 'html.parser')
    text = ""

    #real_site = soup.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "span", "a", "ul", "ol", "li"])

    links = soup.find_all("a")
    for tag in links:
        link_text = Fore.BLUE + str(tag.text.strip())
        text += link_text
    not_links = soup.find_all(["header", "p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "ol", "li"])
    for tag in not_links:
        tag_text = str(tag.text.strip())
        text += tag_text

    full_path = os.path.join(dir, file_name)
    file_exists = os.access(full_path, os.F_OK)
    if file_exists:
        file = open(full_path, "r")
        print(file.read())
        file.close()
    else:

        f = open(full_path, "w", encoding='utf-8')
        f.write(text)
        f = open(full_path, "r", encoding='utf-8')
        print(f.read())
        f.close()


def start():
    # if not create a dir
    dir_exist(dir, dir_exists)

    check()


start()
