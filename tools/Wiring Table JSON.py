import json



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
        # Set alphabet variable; Example: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.alphabet = alphabet
        # Loop over the wiring string
        for char in wiring:
            # Append the index of that char in the alphabet to the wiring varibale of the rotor; Examples: A=0, B=1
            self.wiring.append(self.alphabet.index(char))
        # WER identifier; Example: "ETW", "NORMAL"
        self.wer = wer
        # Notch postions; Examples: "Z", "M"
        self.notches = []
        # Loop over chars (Notch positions) in notches variable
        for char in notch:
            # Add that as an integer to notches
            self.notches.append(alphabet.index(char))

rotors = [
  {
    "Model": "Enigma B",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",
    "Notch": "A",
    "Wiring": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
  },
  {
    "Model": "Enigma B",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",
    "Notch": "Ä",
    "Wiring": "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA"
  },
  {
    "Model": "Enigma B",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",
    "Notch": "Ä",
    "Wiring": "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ"
  },
  {
    "Model": "Enigma B",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",
    "Notch": "Ä",
    "Wiring": "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL"
  },
  {
    "Model": "Enigma B",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ",
    "Notch": "A",
    "Wiring": "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY"
  },
  {
    "Model": "Enigma D",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Enigma D",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Y",
    "Wiring": "LPGSZMHAEOQKVXRFYBUTNICJDW"
  },
  {
    "Model": "Enigma D",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "SLVGBTFXJQOHEWIRZYAMKPCNDU"
  },
  {
    "Model": "Enigma D",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "N",
    "Wiring": "CJGDPSHKTURAWZXFMYNQOBVLIE"
  },
  {
    "Model": "Enigma D",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Enigma K",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Enigma K",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Y",
    "Wiring": "LPGSZMHAEOQKVXRFYBUTNICJDW"
  },
  {
    "Model": "Enigma K",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "SLVGBTFXJQOHEWIRZYAMKPCNDU"
  },
  {
    "Model": "Enigma K",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "N",
    "Wiring": "CJGDPSHKTURAWZXFMYNQOBVLIE"
  },
  {
    "Model": "Enigma K",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Enigma I",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  },
  {
    "Model": "Enigma I",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Q",
    "Wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  },
  {
    "Model": "Enigma I",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  },
  {
    "Model": "Enigma I",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "V",
    "Wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  },
  {
    "Model": "Enigma I",
    "Wheel": "IV",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "J",
    "Wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  },
  {
    "Model": "Enigma I",
    "Wheel": "V",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Z",
    "Wiring": "VZBRGITYUPSDNHLXAWMJQOFECK"
  },
  {
    "Model": "Enigma I",
    "Wheel": "UKW_A",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "EJMZALYXVBWFCRQUONTSPIKHGD"
  },
  {
    "Model": "Enigma I",
    "Wheel": "UKW_B",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
  },
  {
    "Model": "Enigma I",
    "Wheel": "UKWAC",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Q",
    "Wiring": "WTOKASUYVRBXJHQCPZEFMDINLG"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "GJLPUBSWEMCTQVHXAOFZDRKYNI"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "V",
    "Wiring": "JWFMHNBPUSDYTIXVZGRQLAOEKC"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "IV",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "J",
    "Wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "V",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Z",
    "Wiring": "HEJXQOTZBVFDASCILWPGYNMURK"
  },
  {
    "Model": "Norway Enigma (Enigma I variant)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "MOWJYPUXNDSRAIBFVLKZGQCHET"
  },
  {
    "Model": "M3",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  },
  {
    "Model": "M3",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Q",
    "Wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  },
  {
    "Model": "M3",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  },
  {
    "Model": "M3",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "V",
    "Wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  },
  {
    "Model": "M3",
    "Wheel": "IV",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "J",
    "Wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  },
  {
    "Model": "M3",
    "Wheel": "V",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Z",
    "Wiring": "VZBRGITYUPSDNHLXAWMJQOFECK"
  },
  {
    "Model": "M3",
    "Wheel": "VI",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "ZM",
    "Wiring": "JPGVOUMFYQBENHZRDKASXLICTW"
  },
  {
    "Model": "M3",
    "Wheel": "VII",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "ZM",
    "Wiring": "NZJHGRCXMYSWBOUFAIVLPEKQDT"
  },
  {
    "Model": "M3",
    "Wheel": "VIII",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "ZM",
    "Wiring": "FKQHTLXOCBJSPDZRAMEWNIUYGV"
  },
  {
    "Model": "M3",
    "Wheel": "UKW_B",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "YRUHQSLDPXNGOKMIEBFZCWVJAT"
  },
  {
    "Model": "M3",
    "Wheel": "UKW_C",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "FVPJIAOYEDRZXWGCTKUQSBNMHL"
  },
  {
    "Model": "M4",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  },
  {
    "Model": "M4",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Q",
    "Wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
  },
  {
    "Model": "M4",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE"
  },
  {
    "Model": "M4",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "V",
    "Wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO"
  },
  {
    "Model": "M4",
    "Wheel": "IV",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "J",
    "Wiring": "ESOVPZJAYQUIRHXLNFTGKDCMWB"
  },
  {
    "Model": "M4",
    "Wheel": "V",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Z",
    "Wiring": "VZBRGITYUPSDNHLXAWMJQOFECK"
  },
  {
    "Model": "M4",
    "Wheel": "VI",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "ZM",
    "Wiring": "JPGVOUMFYQBENHZRDKASXLICTW"
  },
  {
    "Model": "M4",
    "Wheel": "VII",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "ZM",
    "Wiring": "NZJHGRCXMYSWBOUFAIVLPEKQDT"
  },
  {
    "Model": "M4",
    "Wheel": "VIII",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "ZM",
    "Wiring": "FKQHTLXOCBJSPDZRAMEWNIUYGV"
  },
  {
    "Model": "M4",
    "Wheel": "Beta",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "LEYJVCNIXWPBQMDRTAKZGFUHOS"
  },
  {
    "Model": "M4",
    "Wheel": "Gamma",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "FSOKANUERHMBTIYCWLQPZXVGJD"
  },
  {
    "Model": "M4",
    "Wheel": "UKW_b",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "ENKQAUYWJICOPBLMDXZVFTHRGS"
  },
  {
    "Model": "M4",
    "Wheel": "UKW_c",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "RDOBJNTKVEHMLFCWZAXGYIPSUQ"
  },
  {
    "Model": "Zählwerk Enigma A28",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Zählwerk Enigma A28",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "SUVWZABCEFGIKLOPQ",
    "Wiring": "LPGSZMHAEOQKVXRFYBUTNICJDW"
  },
  {
    "Model": "Zählwerk Enigma A28",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "STVYZACDFGHKMNQ",
    "Wiring": "SLVGBTFXJQOHEWIRZYAMKPCNDU"
  },
  {
    "Model": "Zählwerk Enigma A28",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "UWXAEFHKMNR",
    "Wiring": "CJGDPSHKTURAWZXFMYNQOBVLIE"
  },
  {
    "Model": "Zählwerk Enigma A28",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Zählwerk Enigma (Enigma G)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Zählwerk Enigma (Enigma G)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "SUVWZABCEFGIKLOPQ",
    "Wiring": "LPGSZMHAEOQKVXRFYBUTNICJDW"
  },
  {
    "Model": "Zählwerk Enigma (Enigma G)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "STVYZACDFGHKMNQ",
    "Wiring": "SLVGBTFXJQOHEWIRZYAMKPCNDU"
  },
  {
    "Model": "Zählwerk Enigma (Enigma G)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "UWXAEFHKMNR",
    "Wiring": "CJGDPSHKTURAWZXFMYNQOBVLIE"
  },
  {
    "Model": "Zählwerk Enigma (Enigma G)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "SUVWZABCEFGIKLOPQ",
    "Wiring": "DMTWSILRUYQNKFEJCAZBPGXOHV"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "STVYZACDFGHKMNQ",
    "Wiring": "HQZGPJTMOBLNCIFDYAWVEUSRKX"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "UWXAEFHKMNR",
    "Wiring": "UQNTLSZFMREHDPXKIBVYGJCWOA"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "RULQMZJSYGOCETKWDAHNBXPVIF"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "SUVWZABCEFGIKLOPQ",
    "Wiring": "RCSPBLKQAUMHWYTIFZVGOJNEXD"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "STVYZACDFGHKMNQ",
    "Wiring": "WCMIBVPJXAROSGNDLZKEYHUFQT"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "UWXAEFHKMNR",
    "Wiring": "FVDHZELSQMAXOKYIWPGCBUJTNR"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "SUVWZABCEFGIKLOPQ",
    "Wiring": "WLRHBQUNDKJCZSEXOTMAGYFPVI"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "STVYZACDFGHKMNQ",
    "Wiring": "TFJQAZWMHLCUIXRDYGOEVBNSKP"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "?",
    "Wiring": "?"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "IV",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "?",
    "Wiring": "?"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "V",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "SWZFHMQ",
    "Wiring": "QTPIXWVDFRMUSLJOHCANEZKYBG"
  },
  {
    "Model": "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "KZROUQHYAIGBLWVSTDXFPNMCJE"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "WZEKQ",
    "Wiring": "KPTYUELOCVGRFQDANJMBSWHZXI"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "WZFLR",
    "Wiring": "UPHZLWEQMTDJXCAKSOIGVBYFNR"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "WZEKQ",
    "Wiring": "QUDLYRFEKONVZAXWHMGPJBSICT"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "IV",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "WZFLR",
    "Wiring": "CIWTBKXNRESPFLYDAGVHQUOJZM"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "V",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "YCFKR",
    "Wiring": "UAXGISNJBVERDYLFZWTPCKOHMQ"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "VI",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "XEIMQ",
    "Wiring": "XFUZGALVHCNYSEWQTDMRBKPIOJ"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "VII",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "YCFKR",
    "Wiring": "BJVFTXPLNAYOZIKWGDQERUCHSM"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "VIII",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "XEIMQ",
    "Wiring": "YMTPNZHWKODAJXELUQVGCBISFR"
  },
  {
    "Model": "Enigma T (Tirpitz)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "GEKPBTAUMOCNILJDXZYFHWVQSR"
  },
  {
    "Model": "Enigma K (Swiss Commercial)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Enigma K (Swiss Commercial)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Y",
    "Wiring": "LPGSZMHAEOQKVXRFYBUTNICJDW"
  },
  {
    "Model": "Enigma K (Swiss Commercial)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "SLVGBTFXJQOHEWIRZYAMKPCNDU"
  },
  {
    "Model": "Enigma K (Swiss Commercial)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "N",
    "Wiring": "CJGDPSHKTURAWZXFMYNQOBVLIE"
  },
  {
    "Model": "Enigma K (Swiss Commercial)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Enigma K (Swiss Air Force)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Enigma K (Swiss Air Force)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Y",
    "Wiring": "PEZUOHXSCVFMTBGLRINQJWAYDK"
  },
  {
    "Model": "Enigma K (Swiss Air Force)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "ZOUESYDKFWPCIQXHMVBLGNJRAT"
  },
  {
    "Model": "Enigma K (Swiss Air Force)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "N",
    "Wiring": "EHRVXGAOBQUSIMZFLYNWKTPDJC"
  },
  {
    "Model": "Enigma K (Swiss Air Force)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "IMETCGFRAYSQBZXWLHKDVUPOJN"
  },
  {
    "Model": "Enigma Railway (Rocket)",
    "Wheel": "ETW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QWERTZUIOASDFGHJKPYXCVBNML"
  },
  {
    "Model": "Enigma Railway (Rocket)",
    "Wheel": "I",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "Y",
    "Wiring": "JGDQOXUSCAMIFRVTPNEWKBLZYH"
  },
  {
    "Model": "Enigma Railway (Rocket)",
    "Wheel": "II",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "E",
    "Wiring": "NTZPSFBOKMWRCJDIVLAEYUXHGQ"
  },
  {
    "Model": "Enigma Railway (Rocket)",
    "Wheel": "III",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "N",
    "Wiring": "JVIUBHTCDYAKEQZPOSGXNRMWFL"
  },
  {
    "Model": "Enigma Railway (Rocket)",
    "Wheel": "UKW",
    "Alphabet": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "Notch": "A",
    "Wiring": "QYHOGNECVPUZTFDJAXWMKISRBL"
  },
  {
    "Model": "Enigma Z",
    "Wheel": "ETW",
    "Alphabet": "1234567890",
    "Notch": "A",
    "Wiring": "1234567890"
  },
  {
    "Model": "Enigma Z",
    "Wheel": "I",
    "Alphabet": "1234567890",
    "Notch": "9",
    "Wiring": "6418270359"
  },
  {
    "Model": "Enigma Z",
    "Wheel": "II",
    "Alphabet": "1234567890",
    "Notch": "9",
    "Wiring": "5841097632"
  },
  {
    "Model": "Enigma Z",
    "Wheel": "III",
    "Alphabet": "1234567890",
    "Notch": "9",
    "Wiring": "3581620794"
  },
  {
    "Model": "Enigma Z",
    "Wheel": "UKW",
    "Alphabet": "1234567890",
    "Notch": "9",
    "Wiring": "5079183642"
  }
]

wheels = []

for i in range(0, len(rotors)):
    json_string = json.dumps(rotors[i])
    json_load = json.loads(json_string)

    # rotor("ETW", "1930", "Enigma I", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", alphabet, "ETW", ["A"])
    wiring = json_load["Wiring"]
    if wiring == "?":
        continue
    notch = json_load["Notch"]
    alphabet = json_load["Alphabet"]
    notches = []
    for char in notch:
        notches.append(char)
    if json_load["Wheel"] in ["ETW", "UKW", "GRW"]:
        notches = [alphabet[0]]
    # wheels.append("rotor(\"%s\", \"-\", \"%s\", \"%s\", \"%s\", \"%s\", \"%s\")"  % (json_load["Wheel"], json_load["Model"], json_load["Wiring"], json_load["Alphabet"], json_load["Wheel"], notches))
    # (, json_load["Model"], json_load["Wiring"], json_load["Alphabet"], json_load["Wheel"], notches)
    wer = ""
    if not json_load["Wheel"] in ["ETW", "UKW", "GRW"]:
        wer = "NORMAL"
    wheel = json_load["Wheel"]
    model = json_load["Model"]
    print("______")
    print(wheel)
    print(model)
    print(wiring)
    print(alphabet)
    print(wer)
    print(notches)
    print("______")
    wheels.append(rotor(wheel, "-", model, wiring, alphabet, wer, notches))


for wheel in wheels:
    print(wheel)