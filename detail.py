import os
from time import sleep
from selenium import webdriver

def get_html_with_selenium(url):
    driver = webdriver.Firefox()
    # driver.set_window_size(1, 1)
    driver.get(url)
    sleep(3)
    html = driver.page_source
    driver.close()
    print 'open with selenium: %s' % url
    return html.encode('utf-8')

f = open('game_detail_url')

line = 1

while line:
    line = f.readline()

    line = line.replace('\n', '')
    line = line.replace('\r', '')
    if line == "":
        continue

    url = "https://vk.sportsbull.jp" + line
    print url

    dir = "detail/" + line
    file = dir + "detail"

    try:
        os.makedirs(dir)
    except OSError:
        print 'already exists'

    html = ""
    try:
        html = get_html_with_selenium(url)
    except:
        html = "Failed"

    with open(file, mode='w') as f2:
        f2.write(html)

f.close()


