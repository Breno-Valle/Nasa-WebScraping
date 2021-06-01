from folder_menager import dir_picture_path
import os
import struct
import ctypes

# Mycrosoft System Parameter to set Wallpaper
SPI_SETDESKWALLPAPER = 20

# Paths to Main images (Wallpaper image)
picture_folder = dir_picture_path('Nasa_images')
wallpaper_path = os.path.abspath(picture_folder + '\\nasa.jpg')


def is_64():
    # Return the size of the struct
    # struct.calcsize('P') calculates the number of bytes required to store a single pointer
    # return True or False
    return struct.calcsize('P') * 8 == 64


def get_system_param_info():
    # If the cpu is 64 bits return W, if 32bits return A
    return ctypes.windll.user32.SystemParametersInfoW if is_64() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    # change the wallpaper
    sys_parameters_info = get_system_param_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, wallpaper_path, 3)

    print('>>>New wallpaper displayed')

    if not r:
        print(ctypes.WinError())


def screen_size():
    # GetSystemMetrics return the width and the height of the current screen
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return screensize[0], screensize[1]




