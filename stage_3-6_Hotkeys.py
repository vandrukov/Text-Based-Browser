import os
import argparse

nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created "soft" magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
supported_pages = ["nytimes", "bloomberg"]
parser = argparse.ArgumentParser()
parser.add_argument("ingredient_1")
args = parser.parse_args()
dir = args.ingredient_1
dir_exists = os.access(dir, os.F_OK)
web_page = input()
history = list()
last_page = ""




def dir_exist(dir, dir_exists):
    if not dir_exists:
        # create the dir
        os.makedirs(dir)


def check():
    global web_page
    global last_page
    while web_page != "exit":
        if web_page not in supported_pages:
            if web_page == "exit":
                break
            elif web_page == "back":
                if history:
                    web_page = history.pop()
                    file_esist()
            elif web_page.replace(".com", "") in supported_pages:
                if last_page:
                    history.append(last_page)
                    last_page = ""
                web_page = web_page.replace(".com", "")
                file_esist()
                last_page = web_page
            else:
                print("Invalid URL")
        else:
            if last_page:
                history.append(last_page)
                last_page = ""
            file_esist()
            last_page = web_page

        web_page = input()


def file_esist():
    full_path = os.path.join(dir, web_page)
    file_exists = os.access(full_path, os.F_OK)
    if file_exists:
        file = open(full_path, "r")
        print(file.read())
        file.close()
    else:
        f = open(full_path, "w")
        f.write(nytimes_com) if web_page == "nytimes" else f.write(bloomberg_com)
        f = open(full_path, "r")
        print(f.read())
        f.close()


def start():
    dir_exist(dir, dir_exists)
    check()


start()
