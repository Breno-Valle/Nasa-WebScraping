import PySimpleGUI as sg
from folder_menager import dir_picture_path
from scrapping import scrapping_text, is_video
import os
from PIL import Image

# path to temporary image's folder
picture_folder = dir_picture_path('Nasa_images')


def GUI():
    wallpaper_path = os.path.abspath(picture_folder + '\\nasa_gui.jpg')
    name_img, clean_description = scrapping_text()

    if is_video() == 'no':
        #take the image, resize and made it a PNG file
        image = Image.open(wallpaper_path)
        image.thumbnail([400,512])
        image.save(picture_folder + '\\nasa_gui.png')

        #change the color theme of the GUI
        sg.theme('DarkBlue4')

        # separate two columns, one for text information and other for the image
        text_column = [[sg.Text(f'TITLE: {name_img}')],
                  [sg.Text(clean_description)]]

        image_column = [[sg.Text('Original Image:')],
                        [sg.Image(os.path.abspath(picture_folder + '\\nasa_gui.png'))],
                        [sg.Text('Picture credits on:')],
                        [sg.Text('https://apod.nasa.gov/apod/astropix.html')]]

        # join the two columns in only one layout
        layout = [[sg.Column(text_column),
                   sg.VSeparator(),
                   sg.Column(image_column)]]

        #display windown
        window = sg.Window('Astronomy Picture of the Day', layout, margins=(10,10))

        # only closes if the user close the windown
        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break

    else:
        sg.theme('DarkBlue4')
        layout = [[sg.Text("Unable to Display a video. Yesterday's picture will be displayed")],
                  [sg.Text("If your're using the app for the first time, try again tomorrow. I'm sorry :(")]]
        window = sg.Window('Astronomy Picture of the Day', layout, margins=(10,10))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                break