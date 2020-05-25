from enigmas import enigmas
from steckbrett import steckbrett
import random

def S(letter, i):
    WALZEN = [
        2,
        1,
        0,
        8,
        9
    ]
    alpabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    SETTINGS = [
        [alpabet[0], alpabet[0]],
        [alpabet[0], alpabet[0]],
        [alpabet[0], alpabet[0]],
        [alpabet[0], alpabet[0]],
        [alpabet[0], alpabet[0]]
    ]
    STECKBRETT = [
    ]
    ENIGMA = enigmas.M3.ENIGMA
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    for j in range(0, i + 1):
        ENIGMA.enc("A")
    return ENIGMA.enc(letter)


def P(letter, s):
    return s.enc(letter)
def set_P(letters, s):
    s.add_stecker(letters)



alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
s = steckbrett(alphabet)
msg = "WSNPNLKLSTCS"
pln = "ATTACKATDAWN"
# Make guess
ranin = random.randint(0, len(alphabet))
# Set to what wikipedia says for now
ranin = 24
guess = "".join(["A", alphabet[ranin]])
set_P(guess, s)
#
p = P("A", s)
c = []
for i in range(0, 200):
    c.append(P(S(p, i), s))

print(c)

