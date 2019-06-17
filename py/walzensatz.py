

class walzensatz(object):
    '''Walzensatz object representing a collection of walzen'''
    def __init__(self, walzen):
        '''Initalize Walzensatz object'''
        # Set walzen variable, NORMAL walzen will be added to this array
        self.walzen = []
        # Set GRW variable, GRW walzen (Griechenwalze; This is specific to M4, it doesn't turn)
        self.GRW = []
        # Loop over walzen
        for walze in walzen:
            # If the current Walze is an ETW
            if walze.rotor.wer == "ETW":
                # Set ETW variable to current Walze
                self.ETW = walze
            # If the current Walze is a UKW
            elif walze.rotor.wer == "UKW":
                # Set UKW variable to current Walze
                self.UKW = walze
            # If current Walze is a Griechenwalze 
            elif walze.rotor.wer == "GRW":
                # Add current Walze to GRW array
                self.GRW.append(walze)
            # If current Walze is a normal Walze
            elif walze.rotor.wer == "NORMAL":
                # Add current Walze to walzen array
                self.walzen.append(walze)
        if not hasattr(self, "ETW") or not hasattr(self, "UKW"):
            print("ETW or UKW missing.")
            exit()
    def rotate_doublestepping(self, rotations):
        '''This will simulate the double stepping anomaly, making the simulator accurate for historical enigmas'''
        # If the first rotor is at notch postion
        if rotations[0] in self.walzen[0].notches:
            # Rotate the second rotor
            self.walzen[1].rotate()
        # If the second rotor is at notch position
        if rotations[1] in self.walzen[1].notches:
            # Rotate the second and third rotor
            self.walzen[1].rotate()
            self.walzen[2].rotate()
        # Rotate the first rotor in any case
        self.walzen[0].rotate()
    def rotate_normal(self, rotations):
        '''Rotate the Walzen without double stepping'''
        # We need to rotate the first Walze every time
        self.walzen[0].rotate()
        # Loop over all remaining Walzen
        for i in range(0, len(self.walzen)):
            # If the previous Walze is in notch position
            if rotations[i - 1] in self.walzen[i - 1].notches:
                # Rotate the current Walze
                self.walzen[i].rotate()
            # If the previous Walze is not in notch position, interrupt
            else:
                break
    def rotate(self):
        '''Rotate all walzen'''
        # This variable will contain the rotation variables of all Walzen in the Walzensatz
        rotations = []
        # Loop over Walzen in Walzensatz
        for walze in self.walzen:
            rotations.append(walze.rotation)
        # In this case, the Walzensatz contains a normal Enigma
        if len(rotations) == 3:
            # Because we want this to be as historicly accurate as possible, we need to rotate and take the double stepping anomaly into account
            self.rotate_doublestepping(rotations)
        # In this case, the Walzensatz contains an M4 Enigma
        elif len(rotations) == 4 and len(self.GRW) == 1:
            # Here we also need to take double stepping into account
            self.rotate_doublestepping(rotations)
        # If this is not a conventional Enigma
        else:
            # Rotate normaly, meaning without double stepping
            self.rotate_normal(rotations)
    def enc(self, letter):
        '''Encode a letter'''
        # Rotate at begining
        self.rotate()
        # Initalize working variable, this will change with every rotor the letter goes through
        x = self.ETW.enc(letter, False)
        # Loop over normal walzen (Theese are always before any possible GRW)
        for walze in self.walzen:
            # Encode the current letter x in the current rotor
            x = walze.enc(x, False)
        # Loop over Griechenwalzen
        for griechenwalze in self.GRW:
            # Encode current letter x in the current Griechenwalze
            x = griechenwalze.enc(x, False)
        # Pass the letter through the reflector
        x = self.UKW.enc(x, False)
        # Loop over reversed Griechenwalzen because wer're now going in the opposite direction
        for griechenwalze in reversed(self.GRW):
            # Encode current letter x in the current Griechenwalze
            x = griechenwalze.enc(x, True)
        # Loop over reversed normal Walzen because wer're now going in the opposite direction
        for walze in reversed(self.walzen):
            # Encode current letter x in the current rotor
            x = walze.enc(x, True)
        # Put the letter through the ETW and return it
        return self.ETW.enc(x, True)
    def enc_string(self, string):
        '''Encode a string, return the string'''
        # Result string, where encoded chars will be added to
        result = ""
        # Loop over chars in provided string
        for char in string:
            # Add encoded char to result
            result += self.enc(char)
        # Return the result
        return result



