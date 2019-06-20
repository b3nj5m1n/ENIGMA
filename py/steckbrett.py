

class steckbrett(object):
    '''Plugboard object'''
    def __init__(self, alphabet):
        '''Initalize Steckbrett object'''
        # Set alphabet varibale
        self.alphabet = alphabet
        # Initialize Steckbrett array
        self.steckbrett = []
    def add_stecker(self, pair):
        '''Add a stecker to Steckbrett'''
        # Pair can be a string, divide into array of two chars
        pair = [pair[0], pair[1]]
        # Set letter one
        l1 = pair[0]
        # Set letter two
        l2 = pair[1]
        # Set Index vars
        l1i = -1
        l2i = -1
        f1 = False
        f2 = False
        for i in range(0, len(self.alphabet)):
            if not f1 and self.alphabet[i] == l1:
                l1i = i
                self.alphabet = self.alphabet[:i] + self.alphabet[i+1:]
                f1 = True
        for i in range(0, len(self.alphabet)):
            if not f2 and self.alphabet[i] == l2:
                l2i = i
                self.alphabet = self.alphabet[:i] + self.alphabet[i+1:]
                f2 = True
        # Add pair to Steckbrett
        self.steckbrett.append(pair)
    def enc(self, letter):
        '''Encode a letter thorugh the Steckbrett'''
        letter = letter
        result = ""
        for pair in self.steckbrett:
            if pair[0] == letter:
                result = pair[1]
            if pair[1] == letter:
                result = pair[0]
        if result == "":
            return letter
        return result


