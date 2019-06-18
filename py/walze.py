

class walze(object):
    def __init__(self, rotor, ringstellung, grundstellung):
        '''Initalize the walze object'''
        # Set rotor varibale; Containing wiring, alphabet, ...
        self.rotor = rotor
        # Set Ringstellung (As an integer)
        self.ringstellung = self.rotor.alphabet.index(ringstellung)
        # Set rotation varibale to default of 0
        self.rotation = 0
        # Set wiring variable, allowing for easyer accsess and the wiring varibale of the rotor object to be unchanged, thus making it possible to display the original wiring at any time
        self.wiring = self.rotor.wiring
        # Set dot position to position of "A" in current wiring
        self.dot_position = self.rotor.wiring.index(self.rotor.alphabet.index(self.rotor.alphabet[0]))
        # Loop over all letters before Ringstellung (In the alphabet); e.g.: Ringstellung 5: Loop 0, 1, 2, 3, 4
        for i in range(0, self.ringstellung):
            # Set temporary wiring variable
            temp_wiring = self.wiring
            # Set acutall wiring to empty array
            self.wiring = []
            # Loop over integers in temporary wiring
            for i in temp_wiring:
                # Shift the char by one up the alphabet and add that shifted char to wiring varibable
                self.wiring.append((i + 1) % len(self.rotor.alphabet))
            # Add one to dot position
            self.dot_position = (self.dot_position + 1) % len(self.rotor.alphabet)
        # While the letter at the dot position doesn't match with the Ringstellung
        while not self.wiring[self.dot_position] == self.ringstellung:
            # Rotate the wiring
            self.wiring = self.wiring[1:]+self.wiring[:1]
        # Initalize permutations
        self.permutations = []
        # Loop over chars in wiring & alphabet
        for i in range(0, len(self.rotor.alphabet)):
            # Append i (This will be 0 for A, 1 for B and so on) and what evers corresponds to that in the wiring array
            self.permutations.append([i, self.wiring[i]])
        # Convert Grundstellung to integer
        self.grundstellung = self.rotor.alphabet.index(grundstellung)
        # Rotate until rotation matches Grundstellung
        while not self.rotation == self.grundstellung:
            self.rotation = (self.rotation + 1) % len(self.rotor.alphabet)
        # Set notch postions
        self.notches = self.rotor.notches

    def rotate(self):
        '''Rotate rotor by 1; Thus add 1 to rotation'''
        # Only do this if WER is set to NORMAL, because no other rotor rotates
        if self.rotor.wer == "NORMAL":
            # Do addition 1 mod lenght of alphabet
            self.rotation = (self.rotation + 1) % len(self.rotor.alphabet)

    def enc(self, letter, reverse):
        '''Encode letter'''
        # Step 1: Add rotation to the letter
        letter = (letter + self.rotation) % len(self.rotor.alphabet)
        # Step 2: Loop over permutations
        for pair in self.permutations:
            # If reverse (Coming from the reflector)
            if reverse:
                # Look at the second row
                if pair[1] == letter:
                    # Put temporary letter variable to what that letter corresponds to
                    letter = pair[0]
                    # Step 3: Return the letter - the current rotation; Thus shifting down the alphabet
                    return (letter + (-self.rotation)) % len(self.rotor.alphabet)
            else:
                # Look at first row
                if pair[0] == letter:
                    # Put temporary letter variable to what that letter corresponds to
                    letter = pair[1]
                    # Step 3: Return the letter - the current rotation; Thus shifting down the alphabet
                    return (letter + (-self.rotation)) % len(self.rotor.alphabet)
    
