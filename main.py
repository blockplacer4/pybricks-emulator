# main.py
# made based on a original Pybricks Program for the Spike Prime, ^^

from pybricks_sim import PrimeHub, Button
import time
import threading

hub = PrimeHub()

# Placeholder for functions
def einsammelone():
    print("Executing einsammelone()")

# Simulate motors
class Motor:
    def __init__(self, port, direction=1):
        self.port = port
        self.direction = direction
        self.speed = 0

    def run(self, speed):
        self.speed = speed
        print(f"Motor on port {self.port} running at speed {speed}")

    def stop(self):
        self.speed = 0
        print(f"Motor on port {self.port} stopped")

# Simulate ForceSensor
class ForceSensor:
    def __init__(self, port):
        self.port = port

    def pressed(self):
        # For simulation purposes, we'll return False
        return False

# Initialize motors (simulation)
left_motor = Motor('A')
right_motor = Motor('B', direction=-1)  # Direction.COUNTERCLOCKWISE

motor_C = Motor('C')
motor_D = Motor('D')

# Try to initialize the force sensor; handle if it's not connected
try:
    force_sensor = ForceSensor('F')
except:
    force_sensor = None

def turn_motor(motor, direction):
    speed = 500 * direction
    motor.run(speed)

def stop_motor(motor):
    motor.stop()

def write_display(funktionen, index, debugs, brightness_pattern):
    pixels = [[0]*5 for _ in range(5)]
    # Display normal programs
    for count in range(1, len(funktionen) + 1):
        x, y = divmod(count - 1, 5)
        if x >= 5 or y >=5:
            continue  # Skip if out of bounds
        light = 100 if count == index else 75
        pixels[x][y] = light  # Note: in emulator, pixels are accessed as [row][col]
    ncount = len(funktionen)
    # Display debug programs
    for count in range(1, len(debugs) + 1):
        x, y = divmod(count - 1, 5)
        x += 3  # Shift debug programs to the right by 3 columns
        if x >= 5 or y >=5:
            continue  # Skip if out of bounds
        light = 100 if ncount + count == index else brightness_pattern[count - 1]
        pixels[x][y] = light  # Note: in emulator, pixels are accessed as [row][col]
    hub.display.emulator.set_pixels(pixels)

# Define normal functions (placeholders for your actual functions)
funktionen = [einsammelone]

# Define debug items with motors and directions
debugs = [
    (motor_D, -1),
    (motor_D, 1),
    (None, None),                # Placeholder to skip
    (motor_C, -1),
    (motor_C, 1),
    (right_motor, -1),
    (right_motor, 1),
    (None, None),                # Placeholder to skip
    (left_motor, -1),
    (left_motor, 1)
]

# Brightness pattern for the debug programs
brightness_pattern = [45, 45, 0, 75, 75, 75, 75, 0, 45, 45]

index = 1
debounce_time = 0.2  # in seconds
last_action_time = 0
current_motor = None

total_length = len(funktionen) + len(debugs)

def main_loop():
    global index, last_action_time, current_motor
    while True:
        current_time = time.time()
        buttons = set()
        if hub.left_button.is_pressed():
            buttons.add(Button.LEFT)
        if hub.right_button.is_pressed():
            buttons.add(Button.RIGHT)
        if hub.center_button.is_pressed():
            buttons.add(Button.CENTER)

        # Handle left and right button navigation
        if Button.LEFT in buttons and current_time - last_action_time > debounce_time:
            index = index - 1 if index > 1 else total_length
            # Skip placeholders in debug programs
            while index > len(funktionen) and debugs[index - len(funktionen) - 1][0] is None:
                index = index - 1 if index > 1 else total_length
            write_display(funktionen, index, debugs, brightness_pattern)
            last_action_time = current_time
            time.sleep(0.1)
        elif Button.RIGHT in buttons and current_time - last_action_time > debounce_time:
            index = index + 1 if index < total_length else 1
            # Skip placeholders in debug programs
            while index > len(funktionen) and debugs[index - len(funktionen) - 1][0] is None:
                index = index + 1 if index < total_length else 1
            write_display(funktionen, index, debugs, brightness_pattern)
            last_action_time = current_time
            time.sleep(0.1)
        else:
            write_display(funktionen, index, debugs, brightness_pattern)

        # Handle actions
        if index <= len(funktionen):
            # For normal programs
            if Button.CENTER in buttons and current_time - last_action_time > debounce_time:
                # Start your function here
                function_to_start = funktionen[index - 1]
                function_to_start()
                last_action_time = current_time
        else:
            # For debug programs
            debug_index = index - len(funktionen) - 1
            debug_item = debugs[debug_index]
            if debug_item[0] is not None:
                motor, direction = debug_item
                # Simulate force sensor pressed state
                force_pressed = force_sensor.pressed() if force_sensor else False

                if force_pressed:
                    # Start the motor while the force sensor is pressed
                    turn_motor(motor, direction)
                    current_motor = motor
                else:
                    # Stop the motor when the force sensor is released
                    if current_motor is not None:
                        stop_motor(current_motor)
                        current_motor = None
        time.sleep(0.1)

# Start the main loop in a separate thread
thread = threading.Thread(target=main_loop)
thread.daemon = True
thread.start()

# Start the emulator main loop
hub.emulator.mainloop()
