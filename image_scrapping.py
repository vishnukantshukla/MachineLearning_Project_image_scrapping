#first we have to import all required modules
from bs4 import BeautifulSoup
import requests
import urllib.request
urls=['https://www.flipkart.com/search?q=smartphones&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_11_na_na_na&as-pos=1&as-type=RECENT&suggestionId=smartphones%7CMobiles&requestId=5bc07461-475b-43cb-9898-2115417e4a74&as-searchtext=smartphones',]
for url in urls:   

    response = requests.get(url)
# this is a Beautifulsoup library 
    soup = BeautifulSoup(response.content, 'html.parser')

    img_tags = soup.find_all('img',attrs={"class":"_396cs4"})

    print(img_tags)

    image_urls = []
    
    for img in img_tags:
        if 'src' in img.attrs:
            image_urls.append(img['src'])
    save_path='"C:\Users\DELL\OneDrive\Desktop\ML projects\picturw"'

    for i, url in enumerate(image_urls):

        try:
            filename = f'image_{i}.jpg' 
            urllib.request.urlretrieve(url, save_path+filename)
            print(f"Downloaded image {i+1}/{len(image_urls)}")

        except urllib.error.HTTPError:

            print(f"Failed to download image {i+1}/{len(image_urls)}")





            