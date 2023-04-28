# TR-808

## Description
A fun beat making tool that allows you to input sounds, and create music.

## Project goals
I want to learn more about python and other packages such as pygame, by building a playable drum machine.
pygame seems like it has alot of functionality to offer, wish me luck!

## Start it up
- open up terminal at file directory
- activate the virtual enviornment
    - `source .venv/bin/activate`
- install requirements.txt file
    - `pip instal -r requirements.txt`
- run it with this command
    - `python main.py`
- start making your first beat

## Latest Updates
- created the main window
- created the run time parameters
- created draw grid function to update display
- added 2 divisions, one for instrument text, and one to house the lower menu
- added text to the screen

- added beats and instruments variable to build upon in future
- used beats and instruments variables to aid in building correct number of pads vertically and horizontally
- added grid to spacially define non functional pads

- added mouse button down event to allow users to select the pads
- styled the pads to change colors when clicked

- created variables to build playing logic to determine beat sub-divisions and beat length based on FPS
- created variable to determine the active beat
- built a visual that highlights and moves along the active beat
- passed variables to the draw grid function

- added TR-808 authentic sounds
- added play notes function
- passed play notes function to run while loop

- added play/pause button
- added play/pause functionality

- added bpm adjustment options
- added bpm +1, -1, +5, -5 buttons
- added functionality logic in the while loop

- you can now change the beats per measure
- added time signature view
- added + and - options to adjust the number of beats in your loop

- created mute toggle for each instrument
- updated colors based on instrument toggle if muted channel is gray if active channel is green
- passed new variable to draw grid function to help with toggleing colors
- implemented instrument mute toggle logic in run while loop

- added clear pads button and function to reset all pads
- added load and save buttons and function to open up menu
- created file to save beats into and load beats from


## Created By:
|Name|Email|GitHub|
|----|-----|-------|
|David "Lewey" Melchor|dlmelchor12@gmail.com|https://github.com/leweymelchor|
