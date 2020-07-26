import PySimpleGUI as sg
import sys
import os
from PIL import Image
from PIL import GifImagePlugin

from utils.path_utils import BACKGROUND_IMAGES_PATH

if len(sys.argv) == 1:
    event, values = sg.Window('Gif selector',
                    [[sg.Text('Select Gif to convert')],
                    [sg.Text('file name:'), sg.In()],
                    [sg.FileBrowse(),sg.In()],
                    [sg.Open(), sg.Cancel()]]).read(close=True)
    fname = values[1]
    name = values[0]
else:
    fname = sys.argv[1]


if not fname:
    sg.popup("Cancel", "No gif supplied")
    raise SystemExit("Cancelling: no gif supplied")
else:
    gitImage = Image.open(fname)
    print("Get a gif image in: ",fname, "\nis animated: ",gitImage.is_animated,"\nframe count: ",gitImage.n_frames)

    os.mkdir(BACKGROUND_IMAGES_PATH+'/'+name)
    for frame in range(0,gitImage.n_frames):
        gitImage.seek(frame)
        file_name = name+'_'+str(frame)+".png"
        print(file_name)
        newimg = gitImage.resize((1000, 750), Image.ANTIALIAS)
        newimg.save(BACKGROUND_IMAGES_PATH+'/'+name+'/'+file_name)

