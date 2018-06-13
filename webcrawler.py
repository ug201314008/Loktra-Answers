from bs4 import BeautifulSoup
from sys import argv
import urllib.request
import math
import re

def get_number(text):
    regexpre = re.compile(r'\d+')
    number = regexpre.findall(text)
    number = [int(i) for i in num]
    return max(number)


def webcrawler_function(keyword,page_number=None):
    if page_number==None:
        url = 'http://www.shopping.com/products?KW=%s'%(keyword)
        print("\nURL of given webpage is %s"%(url))
        try:
            resp = urllib.request.urlopen(url)
            html = resp.read()
        except urllib.error.URLError as e:
              contents = e.read()
        soup = BeautifulSoup(html)
        try:
            spans = soup.find_all('span', attrs={'class':'numTotalResults'})
            return get_number(spans[0].getText())
        except:
            return "No matches for %s"%(keyword) 
    else:
        url = 'http://www.shopping.com/products~PG-%s?KW=%s'%(page_number,keyword)
        print("\nURL of given webpage is %s"%(url))
        try:
            resp = urllib.request.urlopen(url)
            html = resp.read()
        except urllib.error.URLError as e:
              contents = e.read()
        soup = BeautifulSoup(html)
        try:
            spans = soup.find_all('span', attrs={'class':'quickLookGridItemFullName hide'})
            itemsarray=[]
            for i in spans:
                itemsarray.append(i.getText())
            return items
        except:
            return "No matches for %s"%(keyword)
        

##Name Function defined as main
if _name_=='_main_':
     if len(argv)>3 or len(argv)<=1:
         print("This is not a valid input")
     elif len(argv)==2:
         file_name,keyword = argv
         print webcrawler_function(keyword)
     else:
         filename,keyword,page_number=argv
         print webcrawler_function(keyword,page_number)
         
         
         
