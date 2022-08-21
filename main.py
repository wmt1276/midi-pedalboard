# Author: William Trimble
# Date: 2022-05-20

import sys
import mido
import pyautogui
from osascript import osascript

hotkeyDelay = 0.3   # Delay Used to Allow Macs to Keep Up

# Get Name of MIDI Controller Port
hardware = 'FCB 1010'   # Default is FCB 1010 (my MIDI pedalboard)

# Get Port Name from Command Line Arguments (If Present)
if len(sys.argv) == 2:
    hardware = sys.argv[1]

# Listen for Input from PedalBoard
with mido.open_input(hardware) as inport:
    volume_increment = 6.25
    
    modifiers = {
        2: 'shift',
        3: 'control',
        4: 'option',
        5: 'command'
    }

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

            # Modifier Keys
            elif control <= 5 and control >= 2:
                # Build AppleScript Command
                command_string = """tell application "System Events"\n\tkey """
                
                # Key Up/Down with Pedal
                if value == 127:
                    command_string += 'down '
                else:
                    command_string += 'up '
                
                command_string += modifiers[control]    # Select Command Based on Pedal
                
                command_string += '\nend tell'
                
                osascript(command_string)   # Execute Command

                # NOTE: If a key is held down as the program terminates, it will continue to be held down. This can be tricky to fix, so do not hold down any pedals as you stop the program.

            # Hotkey Macros
            elif control == 6:
                pyautogui.hotkey('command', 'v', interval=hotkeyDelay)
            elif control == 7:
                pyautogui.hotkey('command', 'c', interval=hotkeyDelay)
            elif control == 8:
                pyautogui.hotkey('ctrl', 'shift', '`', interval=hotkeyDelay)
            elif control == 9:
                pyautogui.press('f5')
            elif control == 10:
                pyautogui.hotkey('ctrl', 'c', interval=hotkeyDelay)