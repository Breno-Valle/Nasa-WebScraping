from folder_menager import dir_picture_path
from scrapping import scrapping_img, is_video
from change_background import change_wallpaper
from GUI import GUI
import os
import time
import requests

# temporary folder to save images
picture_folder = dir_picture_path('Nasa_images')

# source page
url = 'https://apod.nasa.gov/apod/astropix.html'
html_text = requests.get(url)


def run_app():
    # if the folder does not exist, create it
    if not os.path.exists(picture_folder):
        print('>>>Creating Folder')
        os.mkdir(picture_folder)

    #check if the conection exists
    if html_text.status_code == 200:
        print('>>>Conected with the server')

        #check if the folder is empty
        print('>>>Check if Folder Exists')
        if len(os.listdir(picture_folder)) == 0:
            print('>>>Folder is Empty. Trying to fill it')

            # check if page display a video. If not, do the standard pipeline
            if is_video() == 'no':
                # try call scrapping function to download and save the images
                try:
                    scrapping_img()
                except AttributeError:
                    raise AttributeError('Unable to download image. The folder is empty. Check your conection with the or send a message for ""breno_valle@outlokk.com"')

                # call change_wallpaper to display the current image
                try:
                    change_wallpaper()
                except WindowsError:
                    raise WindowsError('Unable to chance desktop background. Send a message for "breno_valle@outlook.com"')
            else: print('>>>Image Picture of the Day displays a video, unable to download it. Try to run the app tomorrow')

        # when folder is not empty, remove all files
        else:
            # check if page display a video. If not, do the standard pipeline
            if is_video() == 'no':
                os.remove('Nasa_images\\nasa.jpg')

                try:
                    os.remove('Nasa_images\\nasa_gui.png')
                except:
                    pass

                try:
                    os.remove('Nasa_images\\nasa_gui.jpg')
                except:
                    pass

                # try to call scrapping function to download and save the images
                try:
                    scrapping_img()
                except AttributeError:
                    raise AttributeError('Unable to download image. The folder is empty .Check your conection with the or send a message for "breno_valle@outlokk.com"')

                # call change_wallpaper to display the current image
                try:
                    change_wallpaper()
                except WindowsError:
                    raise WindowsError('Unable to chance desktop background. Send a message for "breno_valle@outlook.com"')

            else:
                print('>>>Image Picture of the Day displays a video, unable to download it. Yesterday picture will be displayed')
    else:
        raise AttributeError('Unable to connect with the server: "Astronomy Picture of the Day')


if __name__ == '__main__':

    run_app()
    time.sleep(1)
    GUI()
