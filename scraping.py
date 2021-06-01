from change_background import screen_size
from folder_menager import dir_picture_path
import requests
from bs4 import BeautifulSoup
import re
from PIL import Image
import io

picture_folder = dir_picture_path('Nasa_images')

def scrapping_img():

    # Astronomy Picture Of The Day URL
    url = 'https://apod.nasa.gov/apod/astropix.html'

    # Requesting and parsing HTML page
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text,'html.parser')

    #Extracting Image's URL
    images = soup.find_all('a')
    for element in str(images).split():
        if element[0:3] == 'src':
            url_img = str(element).split('"')[1]
            full_url_img = ('https://apod.nasa.gov/apod/' + url_img)

            #saving the pic

            w, h = screen_size()

            requested_img = requests.get(full_url_img)
            img_file = io.BytesIO(requested_img.content)

            #save image for wallpaper
            requested_img_jpg = Image.open(img_file)
            requested_img_jpg = requested_img_jpg.resize([w, h])
            requested_img_jpg.save(picture_folder + '\\nasa.jpg')

            #save image for GUI
            requested_img_gui = Image.open(img_file)
            requested_img_gui.save(picture_folder + '\\nasa_gui.jpg')

    print('>>>Image downloaded')


def scrapping_text():
    # Astronomy Picture Of The Day URL
    url = 'https://apod.nasa.gov/apod/astropix.html'

    # Requesting and parsing HTML page
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'html.parser')

    # Extracting Picture Name
    html_name_img = soup.find_all('b')
    html_name_img = str(html_name_img)
    name_img = re.search('<b>(.+?)</b>',html_name_img).group(1)

    #Extracting Picture Description
    html_description_img = soup.find_all('p')
    html_description_img = str(html_description_img)
    html_description = html_description_img.split('<p>')[4]
    clean_description = re.sub('<(.+?)>', '', html_description)
    clean_description = re.sub('</a>','', clean_description)

    # return name_img, clean_description
    return name_img, clean_description


# check if the website displays a video
def is_video():

    # Astronomy Picture Of The Day URL
    url = 'https://apod.nasa.gov/apod/astropix.html'

    # Requesting and parsing HTML page
    html_text = requests.get(url)
    soup = BeautifulSoup(html_text.text, 'html.parser')

    # Search for video tag
    video = soup.find_all('iframe')
    # if video tag is founded return 'yes'
    if video:
        return 'yes'
    else:
        return 'no'
