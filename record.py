import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
import time
import json
import os
import config

def create_folder(folder_name):
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)

class Rec:
    def __init__(self):
        self.count = 0
        self.coordinates = []
        create_folder(config.POKE_NAME)

    def photo(self):
        x, y = pyautogui.position()
        screen_shot = pyautogui.screenshot(region=(x - 9 , y - 9, 18, 18))
        path = '{1}/flag_{0}.png'.format(self.count, config.POKE_NAME)
        screen_shot.save(path)
        self.count = self.count + 1
        infos = {
            "path": path,
            "blink": [],
            "wait": 0,
            "start": None
        }
        self.coordinates.append(infos)

        
    def tick(self):
        last_coordinates = self.coordinates[-1]
        if last_coordinates["start"] is None:
            last_coordinates["start"] = time.time()
        else:
            last_coordinates["wait"] = time.time() - last_coordinates["start"]
            del last_coordinates["start"]


    def blink_position(self):
        x, y = pyautogui.position()
        last_coordinate = self.coordinates[-1]
        last_coordinate["blink"] = [x, y]
        print(last_coordinate)


    def key_code(self, key):
        print(key)
        if key == keyboard.Key.esc:
            with open('{0}/{0}.json'.format(config.POKE_NAME), 'w') as file:
                file.write(json.dumps(self.coordinates))
            return False
            
        if key == keyboard.Key.insert:
            self.photo()
        if key == keyboard.Key.home:
            self.blink_position()
        if key == keyboard.Key.page_up:
            self.tick()


    def start(self):
        with Listener(on_press=self.key_code) as listener:
            listener.join()

record = Rec()
record.start()