# coding: UTF-8
from prettyprint import pp
import bs4

def _get(elems, i):
    info = elems[i].get_text()
    info = info.replace('\n', '')
    info = info.replace('\r', '')
    info = info.encode('utf-8')
    return str(info)

f = open('game_detail_text')

line = 1

header = ["回戦","試合日","球場","先攻","後攻"]
for i in range(1,19):
    header.append("t" + str(i))
for i in range(1,19):
    header.append("b" + str(i))
header.append("t合計")
header.append("b合計")

seiseki = [
    "打数", "安打", "打点", "二塁打", "三塁打", "本塁打", "三振",
    "四死球", "犠打", "盗塁", "残塁", "失策",
    "併殺", "暴投", "ボーク", "捕逸", "打妨"
]
for i in seiseki:
    header.append('t' + i)
for i in seiseki:
    header.append('b' + i)

header.append('URL')
print ','.join(header)

while line:
    line = f.readline()

    line = line.replace('\n', '')
    line = line.replace('\r', '')

    if line == "":
        continue

    html = open(line).read()

    soup = bs4.BeautifulSoup(html, "html.parser")

    csv = []

    # 試合情報
    elems = soup.select('div.mod-headingA02 h2')

    for elem in elems:
        info = elem.get_text()
        info = info.replace('\n', '')
        info = info.replace('\r', '')
        info = info.encode('utf-8')
        info = info.replace('(', ',')
        info = info.replace('　', ',')
        info = info.replace(')', '')

        csv += info.split(',')
        break

    # 対戦高校
    elems = soup.select('table#school-table a')

    for elem in elems:
        info = elem.get_text()
        info = info.replace('\n', '')
        info = info.replace('\r', '')
        info = info.encode('utf-8')

        csv.append(info)

    # ランニングスコア
    elems = soup.select('tr#top-inning-score td')

    l = len(elems)
    for i in range(0,18):

        if i >= l:
            csv.append('')
            continue

        info = elems[i].get_text()
        info = info.replace('\n', '')
        info = info.replace('\r', '')
        info = info.encode('utf-8')

        csv.append(info)

    # ランニングスコア（後攻）
    elems = soup.select('tr#bottom-inning-score td')

    l = len(elems)
    for i in range(0,18):

        if i >= l:
            csv.append('')
            continue

        info = elems[i].get_text()
        info = info.replace('\n', '')
        info = info.replace('\r', '')
        info = info.encode('utf-8')

        csv.append(info)

    # トータルスコア
    elems = soup.select('table#total-score-table td')

    # top
    info = elems[1].get_text()
    info = info.replace('\n', '')
    info = info.replace('\r', '')
    info = info.encode('utf-8')
    csv.append(info)

    # bottom
    info = elems[2].get_text()
    info = info.replace('\n', '')
    info = info.replace('\r', '')
    info = info.encode('utf-8')
    csv.append(info)

    # 成績
    elems = soup.select('div.mod-tableA01 td')

    # top
    for i in range(1, 13):
        csv.append(_get(elems, i))

    csv.append(_get(elems, 27))
    csv.append(_get(elems, 30))
    csv.append(_get(elems, 33))
    csv.append(_get(elems, 36))
    csv.append(_get(elems, 39))

    # bottom
    for i in range(14, 26):
        csv.append(_get(elems, i))

    csv.append(_get(elems, 28))
    csv.append(_get(elems, 31))
    csv.append(_get(elems, 34))
    csv.append(_get(elems, 37))
    csv.append(_get(elems, 40))

    # url
    url = "https://vk.sportsbull.jp" + line
    url = url.replace('detail', '')
    csv.append(url)

    print ','.join(csv)
