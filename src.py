####################
# CAUTION: mciro:bit serial runs on standard Python, not MicroPython.
# Which means it only runs on your computer, and micro:bit should send the serial messages.
####################
# Required Pakcages to be installed

# pip install pyserial
# pip install pynput
####################
# Run this Python script on your computer while micro:bit is connected to USB.
####################

import serial
from pynput.keyboard import Key, Controller

keyboard = Controller()

encoding = 'utf-8'
port = "COM5"  # check out your port
baud = 115200
s = serial.Serial(port)
s.baudrate = baud

if not s.isOpen():
    s.open()


def take_action(result):
    if result == "u":  # up
        keyboard.press(Key.up)
        print("Up is pressed")
        keyboard.release(Key.up)

    if result == "d":  # down
        keyboard.press(Key.down)
        print("Down is pressed")
        keyboard.release(Key.down)


def get_microbit_msg():
    while True:
        i = s.read()
        msg = i.decode(encoding)
        print("msg from micro:bit:::", msg)
        take_action(msg)


if __name__ == "__main__":
    get_microbit_msg()
