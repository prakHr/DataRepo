#Friends found now friendsOfFriends
import time
import http.cookiejar
import urllib.request
import requests
import bs4
#print(requests.__version__)

# Store the cookies and create an opener that will hold them
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))

# Add our headers
opener.addheaders = [('User-agent', 'dfdf')]

linksOfAllFriends=[]

# Install our opener (note that this changes the global opener to the one
# we just made, but you can also just call opener.open() if you want
urllib.request.install_opener(opener)

#first page always gonna reroute us to login page
authentication_url = "https://mbasic.facebook.com/login.php"
# Input parameters we are going to send(give ur email and password)
payload = {
  'email': '',
  'pass': ''
  }
# Use urllib to encode the payload
data = urllib.parse.urlencode(payload).encode('utf-8')

# Build our Request object (supplying 'data' makes it a POST)
req = urllib.request.Request(authentication_url, data)

# Make the request and read the response
resp = urllib.request.urlopen(req)
contents = resp.read()
print(contents)

#Now that we have logged in successfully,we can reroute to friends page
url = "https://mbasic.facebook.com/prakhar.gandhi.1/friends"

"""
function =>recursive in nature
input => url associated with see more friends button
output => goes that url and add friends to linksOfAllFriends
"""
def my_function(url,linksOfAllFriends):

    data=requests.get(url,cookies=cj)
    soup=bs4.BeautifulSoup(data.text,'html.parser')
    
    my_data=soup.find_all("a")
    #i=2
    for x in my_data:#as we don't know the username
        my_href=x.get("href")
        linksOfAllFriends.append(my_href)
        #We can modify the code to fool the site using random time as input in time.sleep()
        #time.sleep(i)
        #i=2*i
        #if i>64:i=2
        
    #print(soup.prettify())
    for i in soup.find_all('a'):
        if i.text.lower()=="see more friends":
            data_soup=soup.find(attrs={"id":"m_more_friends"})
            my_data=data_soup.find("a")
            url=my_data.get("href")
            url='https://mbasic.facebook.com'+url
            #time.sleep(20)
            my_function(url,linksOfAllFriends)
            
        elif i.text!= "Add Friend":
            print(i.text)

    print(linksOfAllFriends)

#gets the html code of the page
data = requests.get(url, cookies=cj)
#parses the html and prettify it
soup = bs4.BeautifulSoup(data.text, 'html.parser')

for x in soup.find_all("a"):
    my_href=x.get("href")
    linksOfAllFriends.append(my_href)
    
#time.sleep(32)
#print(soup.prettify())
z = 0
for i in soup.find_all('a'):
    
    if i.text.lower()=="see more friends":
        data_soup=soup.find(attrs={"id":"m_more_friends"})
        my_data=data_soup.find("a")
        url=my_data.get("href")
        url='https://mbasic.facebook.com'+url
        #print(str(https://mbasic.facebook.com)+url)
        #time.sleep(20)
        my_function(url, linksOfAllFriends)
                
    elif i.text!= "Add Friend":
        print(i.text)

print(listOfAllFriends)
#Now we go to link associated to <a href="link"> Friends<a>

