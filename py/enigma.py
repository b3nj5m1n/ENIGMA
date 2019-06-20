from steckbrett import steckbrett
from walzensatz import walzensatz
from walze import walze

class ENIGMA(object):
    '''Enigma object'''
    def __init__(self, rotors, name="ENIGMA", letter_divion=4):
        '''Initalize ENIGMA object'''
        # Name of the machine
        self.name = name
        # Possible walzen to choose from
        self.possible_rotors = rotors
        # Set letter divsion
        self.n = letter_divion
        # Make sure object is only used after it is created
        self.created = False
    def create_enigma(self, settings, rotors, plugboard):
        '''Create ENIGMA to make object useable; Walzen is array of ints containing the indicies for walzen to use; Steckbrett is array of strings, strings are pairs of two letters'''
        # Initalize walzen array
        self.rotors = []
        # Add walzen of possible walzen at indicies
        for index in rotors:
            self.rotors.append(self.possible_rotors[index])
        # Set walzen var
        self.walzen = []
        # Create walzen
        for i in range(0, len(self.rotors)):
            self.walzen.append(walze(self.rotors[i], settings[i][0], settings[i][1]))
        # Add alphabet varibale
        self.alphabet = self.walzen[0].rotor.alphabet
        # Initalize Steckbrett object
        self.steckbrett = steckbrett(self.alphabet)
        # Add pairs to steckbrett
        for pair in plugboard:
            self.steckbrett.add_stecker(pair)
        # Add walzensatz
        self.walzensatz = walzensatz(self.walzen)
        # Set created var to True
        self.created = True
    def delete_enigma(self):
        '''Delete ENIGMA object'''
        # Delete all attributes and set created to False
        del self.walzen
        del self.alphabet
        del self.steckbrett
        self.created = False
    def enc(self, letter):
        '''Encode single letter'''
        x = self.steckbrett.enc(letter)
        y = self.walzensatz.enc(x)
        z = self.steckbrett.enc(y)
        return z
    def enc_string(self, string):
        '''Encode a string, return the string'''
        # Result string, where encoded chars will be added to
        result = ""
        # Loop over chars in provided string
        for char in string:
            # Add encoded char to result
            result += self.enc(char)
        # Split string into pairs of n (Letter division)
        result = " ".join([result[i:i+self.n] for i in range(0, len(result), self.n)])
        # Return the result
        return result