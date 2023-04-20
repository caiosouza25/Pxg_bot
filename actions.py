import pyautogui
import keyboard
import button
from time import sleep
import config

class Actions:
    def __init__(self):
        pass

    def move(self, imagem_position):
        x, y = pyautogui.center(imagem_position)
        pyautogui.moveTo(x, y, 0.1)
    
    def move_to_and_click(self, imagem_position):
        self.move(imagem_position)
        pyautogui.click()
    
    def exec_hotkey(self, hotkey, delay=0.5):
        zong = True
        if type(hotkey) == list:
            for atack in hotkey:
                if zong == None:
                    return
                keyboard.press(button.key[atack["button"]], atack["delay"])
                zong = pyautogui.locateOnScreen(config.MY_POKEMON_PNG, confidence=0.8)
        else:
            keyboard.press(button.key[hotkey], delay)
    
    def revive(self):
        current_position = pyautogui.position()
        pyautogui.moveTo(config.MY_POKE_POSITION)
        pyautogui.click(button="right")
        self.exec_hotkey('TAB')
        pyautogui.click()
        sleep(0.33)
        pyautogui.click(button="right")
        pyautogui.moveTo(current_position)

    def pokemon_movement(self, time):
        for i in range(time):
            self.exec_hotkey("F11")
            sleep(0.2)

    def pokeball(self, pokemon):
        if pokemon is not None:
            x, y = pyautogui.center(pokemon)
            pyautogui.moveTo(x, y)
            self.exec_hotkey('CAPS')
            sleep(0.2)
    
    def defense_mode(self):
        keyboard.press(button.key['F10'])

    def atack_mode(self):
        keyboard.press(button.key['F9'])
