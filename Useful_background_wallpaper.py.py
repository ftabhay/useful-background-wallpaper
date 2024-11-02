from PIL import Image, ImageDraw, ImageFont
from pynput.keyboard import Listener
from pathlib import Path
import ctypes
import os

home = Path.home()
word = ""
bnr=ctypes.windll.user32.GetSystemMetrics(1)
a = 60
b = 764

maxcou = int(a * (bnr / b))
cou = 0
en = 0
output_image_path = f"{home}\\bg.png"

def get_screen_size():
    """Get the size of the primary display."""
    user32 = ctypes.windll.user32
def create_black_image(size=None):
    """Create a black image and save it to output_image_path."""
    if size is None:
        size = get_screen_size()  # Get screen size if not provided
    img = Image.new('RGB', size, color='black')
    img.save(output_image_path)

def change(text):
    img = Image.open(output_image_path)
    draw = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('arial.ttf', 100)  #
    draw.text((250, 800), text, font=myFont, fill=(255, 0, 0))

    ctypes.windll.user32.SystemParametersInfoW(20, 0, output_image_path, 3)

def on_press(key):
    global word, cou, en
    try:
        if len(str(key)) == 3:
            cou += 1
            en += 1
            word += str(key)[1:-1]
            change(word)
        elif str(key) == "Key.space":
            cou += 1
            en += 1
            word += " "
            change(word)
        elif str(key) == "Key.backspace":
            cou -= 1
            en -= 1
            word = word[:-1]
            change(word)
        if str(key) == "Key.enter" or cou == maxcou:
            word += "\n"
            en += maxcou - cou
            cou = 0
            change(word)
        if en == 534:
            en = 0
            cou = 0
            word = ""
            create_black_image() 

    except Exception as e:
        print(f"Error: {e}")

create_black_image()

with Listener(on_press=on_press) as listener:
    listener.join()
