#!/usr/bin/python

from urllib import urlopen
from bs4 import BeautifulSoup
import cPickle as pickle
from datetime import datetime

links = ['http://downrightnow.com/yahoomail','http://downrightnow.com/gmail','http://downrightnow.com/hotmail']
#picklefile = open('/home/sp/python/drn/drnDict.p','w')
dictlog = pickle.load(open('/home/sp/python/drn/drnDict.p','rb'))

for link in links:
    domain = link[link.rfind('/')+1:]
    html = urlopen(link).read()
    soup = BeautifulSoup(html)
    status = soup.find_all('span')[4].get_text()
    #print(domain, status)
    dictlog[domain].append((datetime.now(),status))
    
pickle.dump(dictlog,open('/home/sp/python/drn/drnDict.p','wb'))
