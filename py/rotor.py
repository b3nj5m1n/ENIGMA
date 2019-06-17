

class rotor(object):
    '''Object representing a rotor'''
    def __init__(self, kind, date, model, wiring, alphabet, wer, notch):
        '''Initalize the rotor object'''
        # Kind indentifier; Examples: "VIII", "UKW B"
        self.kind = kind
        # Date indentifier; Examples: "1939", "15.12.1938"
        self.date = date
        # Model identifier; Examples: "Enigma I", "M3"
        self.model = model
        # Wiring variable; Example: "[4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]"
        self.wiring = []
        # Loop over the wiring string
        for char in wiring:
            # Append the index of that char in the alphabet to the wiring varibale of the rotor; Examples: A=0, B=1
            self.wiring.append(alphabet.index(char))
        # Set alphabet variable; Example: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet = alphabet
        # WER identifier; Example: "ETW", "NORMAL"
        self.wer = wer
        # Notch postions; Examples: "Z", "M"
        self.notches = []
        # Loop over chars (Notch positions) in notches variable
        for char in notch:
            # Add that as an integer to notches
            self.notches.append(alphabet.index(char))