import sys
import os


# create a temporary path folder
def dir_picture_path(relative_path):

    # sys _MEIPASS create a temporrary folder inside the application
    # this prevent you to have a external directory to save images
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
