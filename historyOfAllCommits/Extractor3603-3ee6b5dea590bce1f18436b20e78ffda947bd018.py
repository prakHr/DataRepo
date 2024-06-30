from bs4 import BeautifulSoup as BS 
import requests,lxml.html
from lxml import etree
from io import BytesIO
import re
'''
iconsName=[
'mobilesv icon-dc',('+')#+,(,),-,1,2,3,4,5,6,7,8,9,0
'mobilesv icon-fe',('(')
'mobilesv icon-ji',('9')
'mobilesv icon-yz',('1')
'mobilesv icon-hg',(')')
'mobilesv icon-ba',('-')
'mobilesv icon-rq',('5')
'mobilesv icon-wx',('2')
'mobilesv icon-nm',('7')
'mobilesv icon-lk',('8')
'mobilesv icon-vu',('3')
'mobilesv icon-acb',('0')
'mobilesv icon-po',('6')
'mobilesv icon-ts',('4')
]'''
#url to fetch
url="https://www.justdial.com/Ahmedabad/Provision-Stores"
agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
html = requests.get(url, headers=agent)
#print (BS(page.content, 'lxml'))
doc = lxml.html.fromstring(html.content)
#el=doc.xpath("//p[@class='contact-info ']/text()")
el=doc.xpath("//p[@class='contact-info ']")
#string="".join(el);#print(string)
#root = etree.Element("root")
#print(el)
#print(el.map{|attr| attr.value})
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

IndividualP=[]  
for e in el:
    count+=1
    #html=etree.Element("html")
    #body = etree.SubElement(html, "body")
    #print(e)
    #tree=(etree.tostring(e, encoding='utf-8'))
    tree=(etree.tostring(e, encoding='unicode'))
    #root = etree.HTML(tree)
    parsed=etree.fromstring(tree)
    
    nodes1=parsed.xpath('/p/span/a/b/span')
    nodes2=parsed.xpath('/p/span/a/span')
    #print(nodes1)
    #print(nodes2)
    #print('-----------')
    if nodes1 ==[]:
        phoneNo=getPhoneNo(nodes2)
    elif nodes2 ==[]:
        phoneNo=getPhoneNo(nodes1)
    #print(phoneNo)  
     
    #body.text=tree
    #print(etree.tostring(html))
    #text_icons=(etree.tostring(html,method="text"))
    #text_icons=html.xpath("string()")
    #text_icons=etree.XPath("class()")
    #print(text_icons)
    #print(tree)
    #root=etree.Element(e,encoding='unicode')
    #print(root)
    #child=root[0]
    #print(root.tag)
    #child=etree.SubElement(root,"i")
    #print(child.tag)
    #print(etree.tostring(e).decode('utf-8'))
    #for article in e:
    #print(etree.tostring(e, pretty_print=True))
    #individualPs=(etree.tostring(e, encoding='utf-8'))
    #lxml.html.fromstring(individualPs)
    #child1=tree.SubElement(individualPs, i class="res_contactic resultimg"))
    #for element in root.iter(tag=etree.e):
      #  print("%s - %s" % (element.tag, element.text))
      
    Paragraphs.append(phoneNo)
    #IndividualP.append(tree)
#print(*IndividualP)
for n in Paragraphs:
    print(n)

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
            
        Paragraphs.append(phoneNo)
    return Paragraphs
    
    
u=''
pageNumbers=50
for i in range(2,pageNumbers+1):
    u=url+'/page-'+str(i)
    phoneNumbers=fetchUrlAndgivePhoneNo(u)
    for n in phoneNumbers:
        print(n)
