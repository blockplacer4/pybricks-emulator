# pybricks_sim.py

from enum import Enum
import time
from emulator import MatrixDisplayEmulator

class Button(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    CENTER = 'middle'

class HubButton:
    def __init__(self, emulator, button_name):
        self.emulator = emulator
        self.button_name = button_name

    def is_pressed(self):
        return self.emulator.button_states.get(self.button_name, False)

class Display:
    def __init__(self, emulator):
        self.emulator = emulator
        self.current_pixels = [[0]*5 for _ in range(5)]

    def pixel(self, x, y, brightness):
        # Aktualisieren Sie ein einzelnes Pixel auf dem Display
        self.current_pixels[y][x] = brightness
        self.emulator.set_pixels(self.current_pixels)

    def clear(self):
        self.current_pixels = [[0]*5 for _ in range(5)]
        self.emulator.clear()

class PrimeHub:
    def __init__(self):
        self.emulator = MatrixDisplayEmulator()
        self.display = Display(self.emulator)
        self.left_button = HubButton(self.emulator, 'left')
        self.right_button = HubButton(self.emulator, 'right')
        self.center_button = HubButton(self.emulator, 'middle')
        self.buttons = self  # Für Kompatibilität