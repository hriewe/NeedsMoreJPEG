# Hayden Riewe
# github.com/hriewe
# hrcyber.tech

# Needs more JPEG GUI version

import PySimpleGUI as sg
from PIL import Image, ImageEnhance, ImageFilter
import sys

# Build layout for homescreen
layout = [[sg.Text('Needs More JPEG', auto_size_text=False, justification='center', font=('Helvetica', 20))],
          [sg.Text('')],
          [sg.Text('Written by Hayden Riewe', auto_size_text=False, justification='center', font=('Helvetica', 20))],
          [sg.Text('')],
          [sg.Text('Select image', size=(20,1)), sg.InputText(size=(35,1)), sg.FileBrowse()],
          [sg.Button('Generate', auto_size_button=True)]]
           

# Show the Window to the user
window = sg.Window('Needs more JPEG!').Layout(layout)

while True:
  button, values = window.Read()

  if button == 'Generate':

    # Open image
    image = Image.open(values[0])

    # Boost saturation
    enhanced = ImageEnhance.Color(image)
    SaturationBoost = enhanced.enhance(4)

    # Boost contrast
    enhanced = ImageEnhance.Contrast(SaturationBoost)
    ContrastBoost = enhanced.enhance(1)

    # Sharpen
    Sharpen = ContrastBoost.filter(ImageFilter.SHARPEN)

    Sharpen.save('NeedsMore.jpeg', quality=5)

    sg.Popup("Image saved succesfully!")