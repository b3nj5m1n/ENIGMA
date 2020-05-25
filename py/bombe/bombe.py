import sys
import rotors
from walze import walze
from walzensatz import walzensatz

class comparer(object):
    # Message should be string, plaintext should be array of strings
    def __init__(self, message, plaintext):
        self.message = message
        self.plaintext = plaintext
    def compare_letters(self, index, plaintext_index):
        return not self.message[index] == self.plaintext[plaintext_index][index % len(self.plaintext[plaintext_index])]
    # Returns true if this is the first letter in the plaintext string
    def is_first(self, index, plaintext_index):
        return 0 == index % len(self.plaintext[plaintext_index])
    def is_last(self, index, plaintext_index):
        return len(self.plaintext[plaintext_index]) - 1 == index % len(self.plaintext[plaintext_index])
    def compare(self, plaintext_index):
        matching = []
        currently_matching = False
        first_index = -1
        for i in range(0, len(self.message)):
            is_first = self.is_first(i, plaintext_index) 
            is_last = self.is_last(i, plaintext_index)
            matches = self.compare_letters(i, plaintext_index)
            currently_matching = matches
            if is_last and matches and currently_matching:
                matching.append(first_index)
            elif is_first and matches:
                first_index = i
            elif not matches:
                currently_matching = False
                first_index = -1
        return matching


class bombe(object):
    def __init__(self, alphabet, message, plaintext):
        self.alphabet = alphabet
        self.message = message
        self.plaintext = plaintext
    def crack(self):
        track = 0
        possibilitys = []
        rotoren = [rotors.historicalrotors.M3.I,
                        rotors.historicalrotors.M3.II,rotors.historicalrotors.M3.III,
                        rotors.historicalrotors.M3.IV,rotors.historicalrotors.M3.V,
                        rotors.historicalrotors.M3.VI,rotors.historicalrotors.M3.VII,
                        rotors.historicalrotors.M3.VIII]
        # Loop over Walzen
        # I-VIII
        for i in range(0, 8):
            # I-VIII
            for j in range(0, 8):
                # I-VIII
                    for l in range(0, 8):
                        # Loop over possible Grundstellungen
                        for x in range(0, len(self.alphabet)):
                            for y in range(0, len(self.alphabet)):
                                for z in range(0, len(self.alphabet)):
                                    walzen = [walze(rotoren[i], "A", self.alphabet[x]),
                     walze(rotoren[j], "A", self.alphabet[y]),
                     walze(rotoren[l], "A", self.alphabet[z]),
                     walze(rotors.historicalrotors.M3.ETW, "A", "A"),
                     walze(rotors.historicalrotors.M3.UKW_B, "A", "A")]
                                    enc = walzensatz(walzen).enc_string(self.message)
                                    track += 1
                                    if self.plaintext in enc:
                                        possibilitys.append(enc)
                                    if track % 100 == 0:
                                        print(track / ((26**3) * (8**3)))
                        for possibility in possibilitys:
                            print(possibility)



def main(args=sys.argv[1:]):

    msg = args[0]
    pln = args[1:]

    # c = comparer(msg, pln)
    # one = c.compare(0)
    # two = c.compare(1)

    b = bombe("ABCDEFGHIJKLMNOPQRSTUVWXYZ", msg, pln[0])
    b.crack()


# GUTENMOINMEINFREUNDWIEYZZKXQNOFHTKQZAYAIIVH
# XVHWCCMBVVNXTDGNSSIKGPYZZKXQNOFHTKQZAYAIIVH


main()