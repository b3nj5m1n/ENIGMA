# Enigma Simulator

## Python

#### A fully featured python implementation of the Enigma machine in python, you can have any number of rotors, change the alphabet, or use historical models (Originally written in June of 2019)

#### Structure

#### enigma.py
##### Main class
###### Functions
**Name** | **Parameters** | **Return** | **Explanation**
:--- | :--- | :--- | :---
init | rotors, name, letter_division=4 |  | Constructor
create_enigma | settings, rotors, plugboard |  | Initializes the enigma
delete_enigma |  |  | Resets the enigma (Reverse of create_enigma)
enc | letter | char | Encodes a single letter
enc_string | string | string | Encodes a string
change_letter_division | new_letter_division |  | Sets a new letter divison
save | output, ret=False | binary dump | Saves the current state or returns it
restore | input |  | Restores machine state from save

#### main.py
##### Example for setting up an enigma and encoding a string

#### rotor.py
##### Object containing all the settings of a rotor
**Name** | **Parameters** | **Return** | **Explanation**
:--- | :--- | :--- | :---
init | kind, date, model, wiring, alphabet, wer, notch |  | Constructor

#### steckbrett.py
##### The Steckbrett
**Name** | **Parameters** | **Return** | **Explanation**
:--- | :--- | :--- | :---
init | alphabet |  | Constructor
add_stecker | pair |  | Adds the pair to the steckbrett
enc | letter | char | Encodes a single letter through the steckbrett

#### walze.py
##### Single Walze
**Name** | **Parameters** | **Return** | **Explanation**
:--- | :--- | :--- | :---
init | rotor, ringstellung, grundstellung |  | Constructor
rotate |  |  | Simluate a single rotation
enc | letter, reverse | char | Encode a letter

#### walzensatz.py
##### A collection of the Walzen of an enigma
**Name** | **Parameters** | **Return** | **Explanation**
:--- | :--- | :--- | :---
init | walzen |  | Constructor
rotate_doublestepping | rotations |  | Rotates and simulates the double stepping anomaly
rotate_normal | rotations |  | Rotates without simulating the double stepping anomaly
rotate |  |  | Rotate as necessary (Takes care of doublestepping)
enc | letter | char | Encodes a single letter
str |  | string | Prints walzen in human readable format
save | output, ret=False | pickle dump | Saves current state of object to file or returns it

#### enigmas.py
##### Presets for (historical) enigmas


#### rotors.py
##### Premade rotor settings (Including historical enigmas)



# You can find the old, original README (With an in-depth explanation of how the Enigma works, from the perspective of a programmer) in the directory other/, either as .md or as a .pdf

