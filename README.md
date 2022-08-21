# MIDI Pedalboard Interface

As a synthisizer player, I am used to using a MIDI pedalboard to augment my playing. I wanted to bring the same experience to software development.
To accomplish this, I have created this Python script to allow my MIDI pedalboard to control my computer.

## Requirements

Development of this project was completed in Python 3.10.4 and has not been tested in any other versions.

I have used the Mido, PyAutoGUI, and OSAScript libraries, which will need to be installed before use.

Development was completed on a Mac with Intel hardware.
The current actions make use of Mac specific controls such as Mac modifier keys (e.g. command instead of control) and AppleScript,
which likely will not work on other computers.
However, one can replace the scripts or keys to suit their own computer needs.

## License

MIT License

Copyright (c) 2022 William Trimble

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
