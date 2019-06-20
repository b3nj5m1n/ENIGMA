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
        8,
        9
    ]
    STECKBRETT = [
        "AU",
        "ZP",
        "LB",
        "KW"
    ]
    ENIGMA = enigmas.M3.ENIGMA
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    print( ENIGMA.enc_string("AAAAAAAAAA") )


# Call the main function at the end of the file
main()