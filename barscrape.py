import requests
import bs4

url = 'https://www.yellowpages.com/london-oh/bars' 

r = requests.get(url) #returns the HTML of the page, can be done through urlopen as well


soup = bs4.BeautifulSoup(r.content)



links = soup.find_all("a")
   
data = soup.find_all("div",{"class":"serp_tp_list"})
listNames=[]
listLoc=[]
count = 1 #To count the first 10 bars

for item in data:

    print item.contents[3]
        
    if count <= 10:
    
    
        print (item.contents[1].find_all("h2",{"class":"listingName"})[0].text) #prints name of bar
        print item.text
        
        print (item.contents[1].find_all("span")[0].text)
        #prints address of bar
        
        print item.contents[3].find_all("h3",{"class":"listingProduct"})[0].text
        
        print item.contents[3].find_all("div",{"class":"phoneDetails"})[0].text
        
         
      
        print item.contents[0].find_all("h3",{"class":"listingProduct"})[0].text 
          
    count+=1
   
data = soup.find_all("div",{"class":"FL serpInrRht bdrL_cdcdcd"})  
count= 1
for item in data:
    if count<=10:
        
        print item.contents[1].find_all("p",{"class":"location"})[0].text
      
    count+=1      

