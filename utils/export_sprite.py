import sys
import os
from PIL import Image
import PySimpleGUI as sg

from utils.path_utils import  SPRINT_IMAGE_PATH

event, values = sg.Window('Gif selector',
                          [[sg.Text('spreadsheet')],
                           [sg.Text('sprite height'), sg.In(default_text = 80)],
                          [sg.Text('sprite width'), sg.In(default_text = 80)],
                           [sg.Text('row number'), sg.In(default_text = 0)],
                           [sg.Text('start image count'), sg.In(default_text = 0)],
                           [sg.Text('end image count'), sg.In()],
                           [sg.Text('sprite name'), sg.In()],
                           [sg.Text('action name'), sg.In()],
                           [sg.FileBrowse(), sg.In()],
                           [sg.Open(), sg.Cancel()]]).read(close=True)

size_height = int(values[0])
size_width = int(values[1])
row_number = int(values[2])
start = int(values[3])
end = int(values[4])
sprite_name = values[5]
action_name = values[6]
image = Image.open(values[7])

if not os.path.exists(SPRINT_IMAGE_PATH+'/'+sprite_name):
    os.mkdir(SPRINT_IMAGE_PATH+'/'+sprite_name)
if not os.path.exists(SPRINT_IMAGE_PATH+'/'+sprite_name+'/'+action_name):
    os.mkdir(SPRINT_IMAGE_PATH+'/'+sprite_name+'/'+action_name)

for i in range(start,end):
    x = size_width*i
    y = row_number*size_height
    file_name = action_name + '_' + str(i) + ".png"
    # left, upper, right, lower
    image.crop((x, y, x+size_width, y+size_height)).save(SPRINT_IMAGE_PATH+'/'+sprite_name+'/'+action_name+'/'+file_name)

