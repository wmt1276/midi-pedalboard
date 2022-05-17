# Author: William Trimble
# Date: 2022-05-16

import mido
import pyautogui
from osascript import osascript

# Listen for Input from PedalBoard
with mido.open_input('FCB 1010') as inport:
    volume_increment = 6.25

    # Handles MIDI Message
    for msg in inport:
        if msg.is_cc() and msg.channel == 0:    # Only Respond to Control Change Messages on Channel 0
            # Get Message Information for Parsing
            control = msg.control
            value = msg.value
            
            if control == 1:    # Mute
                # Mute or Unmute Based on Passed Value
                mute = value != 0
                mute_string = 'set volume output muted '
                
                if mute:
                    mute_string += 'true'
                else:
                    mute_string += 'false'
                
                osascript(mute_string)
            elif control == 3 or control == 5 and value == 127: # Change Volume
                volume = int(osascript('get volume settings')[1].split(', ')[0].replace('output volume:', ''))  # Get Current Volume
                
                # Increase or Decrease Volume Based on Button Pressed
                volume_up = control == 5
                
                if volume_up:
                    volume += volume_increment
                else:
                    volume -= volume_increment
                
                # Change Volume
                volume_string = 'set volume output volume ' + str(volume)
                osascript(volume_string)
                
            elif control == 4:  # Play/Pause Music
                command_string = "tell app \"Spotify\" to playpause"
                osascript(command_string)

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