import sys
from enigmas import enigmas


def main(args=sys.argv[1:]):
    SETTINGS = [
        ["0", "0"],
        ["0", "0"],
        ["0", "0"],
        ["0", "0"],
        ["0", "0"]
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
    ENIGMA = enigmas.Enigma_Z.ENIGMA
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    print( ENIGMA.enc_string("0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000") )


# Call the main function at the end of the file
main()