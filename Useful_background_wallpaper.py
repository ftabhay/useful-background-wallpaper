from pynput.keyboard import Listener
word=""
def on_press(key):
    global word, cou, en
    try:
        if len(str(key)) == 3:
            cou += 1
            en += 1
            word += str(key)[1:-1]
            print(word)
        elif str(key) == "Key.space":
            cou += 1
            en += 1
            word += " "
            print(word)
        elif str(key) == "Key.backspace":
            cou -= 1
            en -= 1
            word = word[:-1]
            print(word)
        if str(key) == "Key.enter" or cou == maxcou:
            word += "\n"
            en += maxcou - cou
            cou = 0
            print(word)
        if en == 534:
            en = 0
            cou = 0
            word = ""
    except Exception as e:
        print(f"Error: {e}")
with Listener(on_press=on_press) as listener:
    listener.join()
