# main.py

from pybricks_sim import PrimeHub, Button
import time
import threading

hub = PrimeHub()

def write_display(funktionen, index):
    pixels = [[0]*5 for _ in range(5)]
    for count, _ in enumerate(funktionen, 1):
        x, y = divmod(count - 1, 5)
        light = 100 if count == index else 75
        pixels[y][x] = light
    hub.display.emulator.set_pixels(pixels)

funktionen = [str(i) for i in range(1, 11)]  # Funktionen von 1 bis 10
index = 1  # Startindex

def main_loop():
    global index
    while True:
        if hub.left_button.is_pressed():
            index = len(funktionen) if index == 1 else index - 1
            print(funktionen[index - 1])
            write_display(funktionen, index)
            time.sleep(0.15)
        if hub.right_button.is_pressed():
            index = 1 if index == len(funktionen) else index + 1
            print(funktionen[index - 1])
            write_display(funktionen, index)
            time.sleep(0.15)
        time.sleep(0.1)  # Kleiner Schlaf, um CPU-Last zu reduzieren

# Starten Sie die Hauptschleife in einem separaten Thread
thread = threading.Thread(target=main_loop)
thread.daemon = True
thread.start()

# Starten Sie die Emulator-Hauptschleife
hub.emulator.mainloop()