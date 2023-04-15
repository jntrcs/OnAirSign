import requests
import psutil
import time
import config

API_KEY = config.API_KEY


def is_camera_active():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if 'CptHost' in proc.info['name']:
                            return True
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            print(psutil.AccessDenied)
            print(psutil.NoSuchProcess)
            pass
    return False

def send_light_off_request():
    url = "https://maker.ifttt.com/trigger/Camera_off/json/with/key/"+API_KEY
    response = requests.get(url)
    return response.status_code

def send_light_on_request():
    url = "https://maker.ifttt.com/trigger/Camera_on/json/with/key/"+API_KEY
    response = requests.get(url)
    return response.status_code

send_light_off_request()
light_state = False

while True:
    if is_camera_active():
        if not light_state:
            send_light_on_request()
            light_state=True
    else:
        if light_state:
            send_light_off_request()
            light_state=False
    time.sleep(10)
