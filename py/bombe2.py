from enigmas import enigmas

SETTINGS = [
        ["A", "A"],
        ["A", "A"],
        ["A", "A"],
        ["A", "A"],
        ["A", "A"]
    ]

STECKBRETT = [
    ]
ENIGMA = enigmas.M3.ENIGMA


msg = "QBXLU GRSZI MTXBG JFSFV RMFOJ YBXNR SBIRQ YZW".replace(" ", "")
pln = "ATTACKATDAWN"

possible = []

stuff = 8*8*8*2*26*25*26
track = 0

for rotor_I in range(0, 8):
    for rotor_II in range(0, 8):
        for rotor_III in range(0, 8):
            for relfector in range(9, 11):
                WALZEN = [
                    rotor_I,
                    rotor_II,
                    rotor_III,
                    8,
                    relfector
                ]
                ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)

                for i in range(0, 26*25*26):
                    track += 1
                    if track % 10000 == 0:
                        print(track / stuff)
                    pos = str(ENIGMA.walzensatz)
                    if ENIGMA.enc(msg[0]) == pln[0]:
                        if ENIGMA.enc(msg[1]) == pln[1]:
                            if ENIGMA.enc(msg[2]) == pln[2]:
                                if ENIGMA.enc(msg[3]) == pln[3]:
                                    if ENIGMA.enc(msg[4]) == pln[4]:
                                        possible.append(str(rotor_I) + str(rotor_II) + str(rotor_III) + pos + str(relfector))

print(possible)