import sys
import rotors
from walze import walze
from walzensatz import walzensatz
# Main function, args varibale will be set to all the arguments supplied, except for the first one because thats just the name of the python file
def main(args=sys.argv[1:]):

    walzen = [walze(rotors.historical_rotors.III, "A", "A"),
    walze(rotors.historical_rotors.II, "A", "A"),
    walze(rotors.historical_rotors.I, "A", "A"),
    walze(rotors.historical_rotors.ETW, "A", "A"),
    walze(rotors.historical_rotors.UKW_B, "A", "A")]
    w = walzensatz(walzen)
    print(w.enc_string("AAAA"))


# Call the main function at the end of the file
main()