import os
import sys
from time import sleep
import psutil
import win32api

for proc in psutil.process_iter(['name']):
    if proc.info['name'] == "DELTARUNE.exe":
        print("please make sure deltarune is closed and relaunch this program")
        sleep(5)
        sys.exit()

dir = os.path.join(os.environ['LOCALAPPDATA'], 'DELTARUNE', "keyconfig_0.ini")

VK_CODE = {8: 'backspace', # i cant believe there are no existing functions that convert keycodes into key names..
 9: 'tab',
 12: 'clear',
 13: 'enter',
 16: 'shift',
 17: 'ctrl',
 18: 'alt',
 19: 'pause',
 20: 'caps_lock',
 27: 'esc',
 32: 'spacebar',
 33: 'page_up',
 34: 'page_down',
 35: 'end',
 36: 'home',
 37: 'left_arrow',
 38: 'up_arrow',
 39: 'right_arrow',
 40: 'down_arrow',
 41: 'select',
 42: 'print',
 43: 'execute',
 44: 'print_screen',
 45: 'ins',
 46: 'del',
 47: 'help',
 48: '0',
 49: '1',
 50: '2',
 51: '3',
 52: '4',
 53: '5',
 54: '6',
 55: '7',
 56: '8',
 57: '9',
 65: 'a',
 66: 'b',
 67: 'c',
 68: 'd',
 69: 'e',
 70: 'f',
 71: 'g',
 72: 'h',
 73: 'i',
 74: 'j',
 75: 'k',
 76: 'l',
 77: 'm',
 78: 'n',
 79: 'o',
 80: 'p',
 81: 'q',
 82: 'r',
 83: 's',
 84: 't',
 85: 'u',
 86: 'v',
 87: 'w',
 88: 'x',
 89: 'y',
 90: 'z',
 96: 'numpad_0',
 97: 'numpad_1',
 98: 'numpad_2',
 99: 'numpad_3',
 100: 'numpad_4',
 101: 'numpad_5',
 102: 'numpad_6',
 103: 'numpad_7',
 104: 'numpad_8',
 105: 'numpad_9',
 106: 'multiply_key',
 107: 'add_key',
 108: 'separator_key',
 109: 'subtract_key',
 110: 'decimal_key',
 111: 'divide_key',
 112: 'F1',
 113: 'F2',
 114: 'F3',
 115: 'F4',
 116: 'F5',
 117: 'F6',
 118: 'F7',
 119: 'F8',
 120: 'F9',
 121: 'F10',
 122: 'F11',
 123: 'F12',
 124: 'F13',
 125: 'F14',
 126: 'F15',
 127: 'F16',
 128: 'F17',
 129: 'F18',
 130: 'F19',
 131: 'F20',
 132: 'F21',
 133: 'F22',
 134: 'F23',
 135: 'F24',
 144: 'num_lock',
 145: 'scroll_lock',
 160: 'left_shift',
 161: 'right_shift ',
 162: 'left_control',
 163: 'right_control',
 164: 'left_menu',
 165: 'right_menu',
 166: 'browser_back',
 167: 'browser_forward',
 168: 'browser_refresh',
 169: 'browser_stop',
 170: 'browser_search',
 171: 'browser_favorites',
 172: 'browser_start_and_home',
 173: 'volume_mute',
 174: 'volume_Down',
 175: 'volume_up',
 176: 'next_track',
 177: 'previous_track',
 178: 'stop_media',
 179: 'play/pause_media',
 180: 'start_mail',
 181: 'select_media',
 182: 'start_application_1',
 183: 'start_application_2',
 186: ';',
 187: '+',
 188: ',',
 189: '-',
 190: '.',
 191: '/',
 192: '`',
 219: '[',
 220: '\\',
 221: ']',
 222: "'",
 246: 'attn_key',
 247: 'crsel_key',
 248: 'exsel_key',
 250: 'play_key',
 251: 'zoom_key',
 254: 'clear_key'}

def get__key():
    print("Please enter any key on your keyboard")
    while True:
        for code in range(256):
            if win32api.GetAsyncKeyState(code) & 0x8000:
                print("you pressed", VK_CODE[code])
                return code

        sleep(0.01)

try:
    question = int(input("Hello! would you like to change enter to space bar (1), enter your own key (2), or revert to default (3): "))
except:
    print("\nyou didnt enter a number, please relaunch this program and try again")
    sleep(5)
    sys.exit()

if question == 1:
    keyCode = 32
elif question == 2:
    sleep(0.5)
    keyCode = get__key()
elif question == 3:
    keyCode = 13
else:
    print("\nyou entered an invalid number, please relaunch this program and try again")
    sleep(5)
    sys.exit()

with open(dir, 'r+') as f:
    lines = f.readlines()
    for i in range(len(lines)):
        if lines[i].startswith("7=") and lines[i] != '7="999.000000"\n':
            lines[i] = f'7="{keyCode}.000000"\n'
    f.seek(0)
    f.writelines(lines)
    f.truncate()
    f.close()

print("patching...") #yes i know this is a fake loading message... but i worry that if it just goes instantly the user gets too little feedback and is left uncertain if it really did work
sleep(2)

print("patched config sucessfully!")
sleep(5)