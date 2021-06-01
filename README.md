# Nasa-WebScraping
This personal program scrapes every day a Nasa Website ("Image Picture of the Day") and change the desktop Wallpaper to the current website Picture

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MOTIVATIONS AND SCRAPING ON INTERNET

I created this program with my girlsfriend idea, to set different scientific and beautiful astronomic images daily as your wallpaper. 
I searched for .robotstxt inside the Astronomic Picture of the Day website and i didn't founded any restrictions about scraping inside their pages.
There is no personal gain with this project and scraping images from nasa. Thats only for joy.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

BRIEF FILES EXPLANATION

With this program you will be able to have a new and fantastic picture of the life, universe and everything (42) as your desktop wallpaper.
Provided by Nasa's website, "Astronomy Picture of the Day", the picture is scrapped and display on your screen. Here is a short explanation about the program:

- folder_menager

This file creates a temporary folder, where the picture will be saved to avoid extra folder creation inside of the user system.
Uses sys lib with '_MEIPASS' to create a temporary folder. To call this function you need to pass the relative path of the picture file.

- scraping.py

This file use Request and BeautifulSoup libs to webscrape the image content of the page and the explanation of the picture as well.
It saves the images into a temporary folder, to be used in another python file. The text content is saved into a variable, called with a function in another python file.

- chamge_background

Using 'ctypes' and 'struct' we are able to interact with th windows system and automaatically change the wallpaper.

It uses ctypes.windll.user32.SystemParametersInfoW if the cpu is 64 bits or ctypes.windll.user32.SystemParametersInfoA if the cpu is 32 bits.
Than, sets the new wallpaper with sys_parameters_info(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3). This requires the folder_menager import to acess the picture.
This file also calculates the current screen size to resize the image to create a better experience to the user.

- GUI

This python file creates a Graphic User Interface to set the picture explanation, provided by the Nasa website (written by a professional Astronomer). to the user.
It also sets the original image of the site, without resizing. With this, the user is able to read and compare it with the image, having a better understanding of the picture.
The main libs used are: PySimpleGUI and Pillow (PIL).


- main

This one is the master file, running other applications in the right sequence, it allows the app to work well. It also deal with the folder menagement and possible exceptions
rised by the system like the 404 HTTP error. This program only runs when required by the user. Future updates are planned to avoid this and run as a Window's schedular task. 

-nasa icon

That is just an .ico file, used when you are transforming these files into an executable windows app.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

TRANFORMING THESE FILES INTO EXECUTABLE:

To do that you need to use Pyinstaller lib. In your console (windows prompt), go to the folder where your files are stored. Inside of it write the following command:

pyinstaller --onefile --noconsole main.py --icon=nasa_icon.ico

This will create a unique executable, with a nasa icon, and no console displaied at your screen.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------





