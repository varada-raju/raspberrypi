from gpiozero import MotionSensor 
from picamera import PiCamera
from datetime import datetime
import time
import os

pir = MotionSensor(4)
camera = PiCamera()
flag = 1;

while True:
    pir.wait_for_motion()
    print("Motion Detected")
    today = datetime.now()
    fon = str('./' + today.strftime('%Y-%m-%d'))
    if today.hour == 0 and today.minute == 0 and today.second == 0:
        os.mkdir(fon)
    elif flag:
        os.mkdir(fon)
        flag = 0
    #dt = str(datetime.datetime.now())
    dt = time.strftime('%Y-%m-%d_%H:%M:%S')
    filename = fon + '/' + 'capture_' + dt + '.jpg'
    #camera.start_preview()
    camera.capture(filename)
    pir.wait_for_no_motion()
    continue
    #camera.close()
    #camera.stop_preview()
