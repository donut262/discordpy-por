import re
from bs4 import BeautifulSoup
import urllib.request, urllib.error
from xml.sax.saxutils import unescape

official_url = 'https://moepic.com'

def get_moe_news(get_all=True):

    except_list = []
    if get_all is False:
        with open('except_news_titles.txt', mode='rb') as f:
            except_list = [s.strip() for s in f.readlines()]

    # HTMLのパース
    html = urllib.request.urlopen(official_url + '/top.php?mid=_')
    soup = BeautifulSoup(html, 'html.parser')
    news = soup.find_all('a', class_='topnews_imp')
    news_list = []

    # topnews_impクラスが存在する場合のみ処理
    if len(news) > 0:
        # タイトルとURLを取り出してリストに入れる
        for row in news:
            pat = "^.+href=\"javascript:Move\(\'(.+)\',\'(.+)\'\)\">(.+)<\/a>"
            repatter = re.compile(pat)
            result = repatter.match(str(row))

            # パターンにマッチした場合だけ処理を実行
            if result is not None:
                url = official_url + result.group(1) + '?hidden_key=' + result.group(2)
                title = unescape(result.group(3))
                news_list.append({'title': title, 'url': url})

    output_list = []
    for d in news_list:
        news_title = d.get('title').encode('utf-8')
        if news_title not in except_list:
            output_list.append(d)

    return output_list
