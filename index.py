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


for year in range(2006, 2019):
    for kind in [300, 400]:

        if year != 2018:
            continue

        url = "https://vk.sportsbull.jp/koshien/game/" + str(year) + "/" + str(kind) + "/"
        dir  = "index/" + str(year) + "/"
        file = dir + str(kind)

        try:
            os.mkdir(dir)
        except OSError:
            print 'already exists'


        print file
        html = get_html_with_selenium(url)

        with open(file, mode='w') as f:
            f.write(html)

