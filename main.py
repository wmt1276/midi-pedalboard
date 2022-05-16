# Author: William Trimble
# Date: 2022-05-16

import mido
import pyautogui
from osascript import osascript

# Listen for Input from PedalBoard
with mido.open_input('FCB 1010') as inport:
    # Dictionary Control Change Values to MOdifier Keys
    modifiers = {
        2: 'shift',
        3: 'ctrl',
        4: 'option',
        5: 'command'
    }

    # Handles MIDI Message
    for msg in inport:
        if msg.is_cc() and msg.channel == 0:    # Only Respond to Control Change Messages on Channel 0
            # Get Message Information for Parsing
            control = msg.control
            value = msg.value
            
            if control == 1:    # Toggle Mute
                # Mute or Unmute Based on Passed Value
                mute = value != 0
                mute_string = 'set volume output muted '
                
                if mute:
                    mute_string += 'true'
                else:
                    mute_string += 'false'
                
                osascript(mute_string)
                
            # Code Below Doesn't Work
            # elif control <= 5:
            #     if value == 127:
            #         pyautogui.keyDown(modifiers[control])
            #     else:
            #         pyautogui.keyUp(modifiers[control])
            
            # Hotkey Macros
            elif control == 6:
                pyautogui.hotkey('command', 'v')
            elif control == 7:
                pyautogui.hotkey('command', 'c')
            elif control == 8:
                pyautogui.hotkey('ctrl', 'shift', '`')
            elif control == 9:
                pyautogui.hotkey('f5')
            elif control == 10:
                pyautogui.hotkey('enter')