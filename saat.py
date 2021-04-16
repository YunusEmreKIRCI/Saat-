import PySimpleGUI as sg
import time
from datetime import datetime

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
layout = [
    [sg.Text(current_time, size=(30, 1),key='saat', font=('Helvetica', 30), justification='center', text_color='red', background_color='black')], ]

window = sg.Window('Saat', background_color='black', font='Helvetica 18').Layout(layout)

while (True):
    event, values = window.read(timeout=0)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    window.FindElement('saat').Update(current_time)
    time.sleep(1)