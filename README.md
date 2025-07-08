This is my code for the OCR GCSE NEA 1 music quiz game.
This project involves a song being chosen and then a 5 second .wav clip of it being played along with the code providing the initials of the song. User then has to guess the song.

To run on any platform you must install all three txt files and edit them as you wish keeping the format the same. Ensure that passwords in the password file are Caesar shifted forwards 6.
Also download all 15 songs and store them with the same name as given in the questions txt file.

then:

For WINDOWS:
download Windows.py and run in python IDE (Definitely works in thonny)

For LINUX:
download Linux.py and run in python IDE (Should work in thonny - may need to sudo install alsa-utils in terminal using "sudo apt install alsa-utils"

For WEB USE:
download Web.py
attach all files into the web IDE of choice
REMOVE KNOCKING ON HEAVEN'S DOOR AND ANY SONG WITH AN APOSTROPHE (') IN THE NAME FROM BOTH Questions.txt AND Songs because the apostrophe messes up IPython by ending the string there
ensure web IDE supports IPython (Definitely works on Jupyter Notebook)
