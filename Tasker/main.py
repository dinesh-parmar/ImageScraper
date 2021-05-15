from bs4 import BeautifulSoup
import requests

URL_LINK="<URL_LINK_HERE>"

body = requests.get(URL_LINK)

soup = BeautifulSoup(body.text, 'html.parser')

list_of_images = soup.find_all('img')
#print(list_of_images)
source = [img['src'] for img in list_of_images]

imageCount=0

for i,link in enumerate(source):
    with open(f"images/images{i+1}.jpg","wb+") as f:
        if ".svg" not in link:
            #print(link)
            if 'http' not in link:
                link = '{}{}'.format(URL_LINK, link)
            response = requests.get(link)
            imageCount+=1
            f.write(response.content)

print("{} images were found".format(imageCount))

