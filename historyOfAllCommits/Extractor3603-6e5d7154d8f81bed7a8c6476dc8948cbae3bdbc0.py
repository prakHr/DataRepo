#Code doesn't account for changing database so empty spaces preferred not to remove or do it manually
from bs4 import BeautifulSoup as BS 
import requests,lxml.html
from lxml import etree
from io import BytesIO
import re


Paragraphs=[]
count=0
def getPhoneNo(nodes):
    phoneNo=''
    for node in nodes:
        icon=node.xpath("@class")
        first_icon=icon[0]
        iconsToNumbers=[
            'mobilesv icon-acb','mobilesv icon-yz',
            'mobilesv icon-wx','mobilesv icon-vu',
            'mobilesv icon-ts','mobilesv icon-rq',
            'mobilesv icon-po','mobilesv icon-nm',
            'mobilesv icon-lk','mobilesv icon-ji']
        
        if first_icon in iconsToNumbers:
            phoneNo+=str(iconsToNumbers.index(first_icon))

        signs=['mobilesv icon-dc','mobilesv icon-fe',
               'mobilesv icon-hg','mobilesv icon-ba']

        if first_icon==signs[0]:phoneNo+='+'
        if first_icon==signs[1]:phoneNo+='('
        if first_icon==signs[2]:phoneNo+=')'
        if first_icon==signs[3]:phoneNo+='-'
    return phoneNo

#url to fetch
def fetchUrlAndgivePhoneNo(url):
    agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
    html = requests.get(url, headers=agent)
    doc = lxml.html.fromstring(html.content)
    el=doc.xpath("//p[@class='contact-info ']")
    for e in el:
        tree=(etree.tostring(e, encoding='unicode'))
        parsed=etree.fromstring(tree)
        nodes1=parsed.xpath('/p/span/a/b/span')
        nodes2=parsed.xpath('/p/span/a/span')
        
        if nodes1 ==[]:
            phoneNo=getPhoneNo(nodes2)
        elif nodes2 ==[]:
            phoneNo=getPhoneNo(nodes1)
        #elif nodes1==[] and nodes2==[]:
          #  phoneNo='empty'
        Paragraphs.append(phoneNo)
    return Paragraphs

#prefer to do a single page piece so that repeated phoneNo doesn't occur(some pages loads the content of previous pages as well due to ajax loading)
def aSinglePageContent(pageNo):
    url_name='https://www.justdial.com/Ahmedabad/Provision-Stores'+'/page-'+str(pageNo)
    phoneNumbers=fetchUrlAndgivePhoneNo(url_name)
    print('-----*Page '+str(pageNo)+'*-----')
    for n in phoneNumbers:
        print(n)

for pages in range(1,50+1):
    SinglePageContent(pages)

    

