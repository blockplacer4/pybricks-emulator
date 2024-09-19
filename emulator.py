import tkinter as tk
import time
import threading

class MatrixDisplayEmulator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SPIKE Prime Emulator")
        self.canvas = tk.Canvas(self.root, width=250, height=250)
        self.canvas.grid(row=0, column=0, columnspan=3)
        self.pixel_size = 50
        self.rects = [[None for _ in range(5)] for _ in range(5)]
        self.create_pixels()

        # Tastenstatus
        self.button_states = {
            'left': False,
            'middle': False,
            'right': False
        }

        # Erstellen der Tasten
        self.create_buttons()

        # Event-Handling für Tasten
        self.root.bind('<KeyPress>', self.key_pressed)
        self.root.bind('<KeyRelease>', self.key_released)

        # Update-Schleife
        self.root.after(100, self.update_buttons)

    def create_pixels(self):
        for y in range(5):
            for x in range(5):
                x0 = x * self.pixel_size
                y0 = y * self.pixel_size
                x1 = x0 + self.pixel_size
                y1 = y0 + self.pixel_size
                rect = self.canvas.create_rectangle(
                    x0, y0, x1, y1,
                    fill="#f5f5dc", outline="gray"  # Helles Beige als Grundfarbe
                )
                self.rects[y][x] = rect
        self.root.update()

    def set_pixels(self, pixels):
        for y in range(5):
            for x in range(5):
                brightness = pixels[y][x]
                color = self.brightness_to_color(brightness)
                self.canvas.itemconfig(self.rects[y][x], fill=color)
        self.root.update()

    def brightness_to_color(self, brightness):
        # Helligkeit in beigen/goldenen Farbton umwandeln
        # Wir variieren die Intensität des Goldtons basierend auf der Helligkeit
        base_color = (245, 245, 220)  # RGB für Beige (#f5f5dc)
        max_color = (255, 215, 0)     # RGB für Gold (#ffd700)

        r = int(base_color[0] + (max_color[0] - base_color[0]) * (brightness / 100))
        g = int(base_color[1] + (max_color[1] - base_color[1]) * (brightness / 100))
        b = int(base_color[2] + (max_color[2] - base_color[2]) * (brightness / 100))

        # Begrenzung der Werte auf 0-255
        r = min(max(r, 0), 255)
        g = min(max(g, 0), 255)
        b = min(max(b, 0), 255)

        return f"#{r:02x}{g:02x}{b:02x}"

    def clear(self):
        self.set_pixels([[0]*5 for _ in range(5)])

    def create_buttons(self):
        self.left_button = tk.Button(self.root, text="Links", width=10)
        self.left_button.grid(row=1, column=0)
        self.left_button.bind('<ButtonPress>', lambda event: self.button_press('left'))
        self.left_button.bind('<ButtonRelease>', lambda event: self.button_release('left'))

        self.middle_button = tk.Button(self.root, text="Mitte", width=10)
        self.middle_button.grid(row=1, column=1)
        self.middle_button.bind('<ButtonPress>', lambda event: self.button_press('middle'))
        self.middle_button.bind('<ButtonRelease>', lambda event: self.button_release('middle'))

        self.right_button = tk.Button(self.root, text="Rechts", width=10)
        self.right_button.grid(row=1, column=2)
        self.right_button.bind('<ButtonPress>', lambda event: self.button_press('right'))
        self.right_button.bind('<ButtonRelease>', lambda event: self.button_release('right'))

    def button_press(self, button):
        self.button_states[button] = True

    def button_release(self, button):
        self.button_states[button] = False

    def key_pressed(self, event):
        if event.keysym == 'Left':
            self.button_states['left'] = True
        elif event.keysym == 'Return':
            self.button_states['middle'] = True
        elif event.keysym == 'Right':
            self.button_states['right'] = True

    def key_released(self, event):
        if event.keysym == 'Left':
            self.button_states['left'] = False
        elif event.keysym == 'Return':
            self.button_states['middle'] = False
        elif event.keysym == 'Right':
            self.button_states['right'] = False

    def update_buttons(self):
        # Aktualisierung der Tastenstatus
        self.root.after(100, self.update_buttons)

    def mainloop(self):
        self.root.mainloop()

