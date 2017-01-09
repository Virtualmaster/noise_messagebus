import sounddevice as sd
import numpy  as np
import requests
import re
from time import sleep

duration = 60  # seconds
delay = 0.05
http_target = "http://localhost:3000/noise_levels"
p = re.compile('(?<=<meta name="csrf-token" content=").*(?=")')
cookies = []
token = ""

def send_to_http(value):
    global cookies, token
    payload = {'authenticity_token': token, 'noise_level[value]': value}
    r = requests.post(http_target, data=payload, cookies = cookies)

def connect_http():
    global cookies, token
    r = requests.get(http_target)
    cookies = r.cookies
    token = p.findall(r.text)[0]

def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    send_to_http(volume_norm)
    sleep(delay)
    print volume_norm

connect_http()
with sd.Stream(callback=print_sound):
    sd.sleep(duration * 1000)
