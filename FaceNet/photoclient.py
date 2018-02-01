# Copyright 2018 Cleuton Sampaio

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import requests
import RPi.GPIO as GPIO
import time
import picamera

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False) 
GPIO.setup(18,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.OUT) # Yellow
GPIO.setup(24,GPIO.OUT) # Green
GPIO.setup(25,GPIO.OUT) # Red
camera = picamera.PiCamera()

def uploadFoto(foto):
    url = 'http://localhost:8088'
    files = {'file': open(foto, 'rb')}
    r = requests.post(url, files=files)
    return r.status_code


def waitFoto():
    input_state = GPIO.input(18)
    if input_state == 0:
        GPIO.output(23,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        GPIO.output(24,GPIO.LOW)
        print('Tirou foto!')
        GPIO.output(23,GPIO.HIGH)
        camera.capture('foto.jpg')
        time.sleep(0.2)
        retorno = uploadFoto('foto.jpg')
        print('*** Retorno do processamento da foto: ', retorno)
        GPIO.output(23,GPIO.LOW)
        if retorno = True:
            GPIO.output(24,GPIO.HIGH)
        else:
            GPIO.output(25,GPIO.HIGH)
        time.sleep(0.2)    
    

while (True):
    waitFoto()