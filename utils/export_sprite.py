import sys
import os
from PIL import Image
import PySimpleGUI as sg

from utils.path_utils import  SPRINT_IMAGE_PATH

event, values = sg.Window('Gif selector',
                          [[sg.Text('spreadsheet')],
                           [sg.Text('sprite height \ width'), sg.In(default_text = 80)],
                           [sg.Text('row number'), sg.In(default_text = 0)],
                           [sg.Text('start image count'), sg.In(default_text = 0)],
                           [sg.Text('end image count'), sg.In()],
                           [sg.Text('sprite name'), sg.In()],
                           [sg.Text('action name'), sg.In()],
                           [sg.FileBrowse(), sg.In()],
                           [sg.Open(), sg.Cancel()]]).read(close=True)

size = int(values[0])
row_number = int(values[1])
start = int(values[2])
end = int(values[3])
sprite_name = values[4]
action_name = values[5]
image = Image.open(values[6])

if not os.path.exists(SPRINT_IMAGE_PATH+'/'+sprite_name):
    os.mkdir(SPRINT_IMAGE_PATH+'/'+sprite_name)
if not os.path.exists(SPRINT_IMAGE_PATH+'/'+sprite_name+'/'+action_name):
    os.mkdir(SPRINT_IMAGE_PATH+'/'+sprite_name+'/'+action_name)

for i in range(start,end):
    x = size*i
    y = row_number*size
    file_name = action_name + '_' + str(i) + ".png"
    # left, upper, right, lower
    image.crop((x, y, x+size, y+size)).save(SPRINT_IMAGE_PATH+'/'+sprite_name+'/'+action_name+'/'+file_name)

