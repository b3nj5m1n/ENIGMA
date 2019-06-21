import sys
from enigmas import enigmas


def main(args=sys.argv[1:]):
    SETTINGS = [
        ["A", "A"],
        ["A", "A"],
        ["A", "A"],
        ["A", "A"],
        ["A", "A"]
    ]
    WALZEN = [
        2,
        1,
        0,
        3,
        4
    ]
    STECKBRETT = [
    ]
    ENIGMA = enigmas.Zählwerk_Enigma_GA111.ENIGMA
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    print( ENIGMA.enc_string("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA") )


# Call the main function at the end of the file
main()