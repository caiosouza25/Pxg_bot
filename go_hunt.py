import pyautogui
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import json
from actions import Actions
from time import sleep
import config


class Hunt:
    def __init__(self):
        self.isStarted = True
        with open('{0}/{0}.json'.format(config.POKE_NAME), 'r') as file:
            infos = file.read()
        self.infos = json.loads(infos)
        self.actions = Actions()


    def go_to_flag(self, item):
        for i in range(10):
            flag_position = pyautogui.locateOnScreen(item['path'], confidence=0.8)
            if flag_position == None:
                return
            self.actions.move_to_and_click(flag_position)
            "self.actions.defense_mode()"
            sleep(item['wait'])

    def do_attack(self, time, item):
        for i in range(time):
            if pyautogui.locateOnScreen('{0}/{0}.png'.format(config.POKE_NAME), confidence=0.8) is None:
                break
            pyautogui.moveTo(item["blink"][0], item["blink"][1], 0.1)
            "self.actions.atack_mode()"
            self.actions.pokemon_movement(3)
            self.actions.exec_hotkey(config.ATACK)
            self.actions.revive()

    def collect_items(self, item):
        pyautogui.moveTo(item["blink"][0], item["blink"][1], 0.1)
        pyautogui.click()
        sleep(6)
        self.actions.exec_hotkey('F12')


    def use_pokeball(self):
        if config.IS_POKEBALL == True and pyautogui.locateOnScreen(config.POKEBALL_PNG, confidence=0.8) is not None:
            for i in range(15):
                pokemon = pyautogui.locateOnScreen('{0}/{0}_dead.png'.format(config.POKE_NAME), confidence=0.8)
                self.actions.pokeball(pokemon)


    def start_route(self):
        while self.isStarted:
            for item in self.infos:
                self.go_to_flag(item)
                self.do_attack(4, item)
                sleep(0.5)
                self.collect_items(item)
                self.use_pokeball()


    def target_key(self, key):
        print(key)
        if key == keyboard.Key.esc:
            return False
        if key == keyboard.Key.delete:
            threading.Thread(target=self.start_route).start()

    def start_keyboard(self):
        with Listener(on_press=self.target_key) as listener:
            listener.join()

hunt = Hunt()

hunt.start_keyboard()


