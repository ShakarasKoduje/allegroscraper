#https://allegro.pl/kategoria/obiektywy-258269?string=pe%C5%82na%20klatka&description=1&bmatch=engag-electro-n-cl-eyesa-bp-ele-1-2-0627
#https://allegro.pl/kategoria/obiektywy-258269?string=pe%C5%82na%20klatka&description=1
#https://allegro.pl/kategoria/obiektywy?string=pe%C5%82na%20klatka&description=1
#https://allegro.pl/kategoria/fotografia?string=pełna klatka&description=1
#

import requests
from bs4 import BeautifulSoup as bs

oferty=[]
pages_list = []
print("test")
url = "https://allegro.pl/kategoria/fotografia?string=pełna klatka&description=1"
r = requests.get(url)
print(r.status_code)
content = r.text
soup = bs(content, 'html.parser')
l = None
pages = soup.find('span',{'class' : 'm-pagination__text'}).getText()
pages = int(pages)
print(f"Stron: {pages}")

for i in range(1,pages+1):
    page_index = f"&p={i}"
    p = url + page_index
    r = requests.get(p)
    #print(f"Strona {p}/ odpowiedź: {r.status_code}")
    pages_list.append(p)



for link in soup.findAll('div', {'class' : 'opbox-listing--base'}):
    l = link
    print(type(l))


Obiektywy = []
for a in l.find_all('article'):
    if a['data-item'] and a['data-analytics-view-custom-index0']:

        oferta = a.find('a').get('href')
        if oferta.startswith('https://allegro.pl/oferta'):
            oferty.append(oferta)
            _r = requests.get(oferta)
            _c = _r.text
            _s = bs(_c, 'html.parser')
            Obiektyw = _s.findAll('span', {'itemprop':'name'})
            #print(Obiektyw)
            for o in Obiektyw:
                str_o = o.getText()
                print(str_o)
                if str_o == 'Obiektywy':
                    print(f"oferta: {oferta}: Kategoria: {o}")
                    print("---------------")
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
            #if Obiektyw.find('Obiektywy') > 0:
                #print(f"oferta: {oferta}: Kategoria: {Obiektyw}")

'''
print("wypisuje linki z tablicy")
print(len(oferty))
for o in oferty: print(o)
'''
