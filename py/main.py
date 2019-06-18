import sys
import rotors
from walze import walze
from walzensatz import walzensatz
# Main function, args varibale will be set to all the arguments supplied, except for the first one because thats just the name of the python file
def main(args=sys.argv[1:]):

    # walzen = [walze(rotors.historical_rotors.III, "A", "A"),
    # walze(rotors.historical_rotors.II, "A", "A"),
    # walze(rotors.historical_rotors.I, "A", "A"),
    # walze(rotors.historical_rotors.ETW, "A", "A"),
    # walze(rotors.historical_rotors.UKW_B, "A", "A")]
    # w = walzensatz(walzen)
    # print(w.enc_string("AAAAA"))

    # walzen = [walze(rotors.historical_rotors.III, "A", "A"),
    # walze(rotors.historical_rotors.II, "A", "A"),
    # walze(rotors.historical_rotors.I, "A", "A"),
    # walze(rotors.historical_rotors.Beta, "A", "A"),
    # walze(rotors.historical_rotors.ETW_M4, "A", "A"),
    # walze(rotors.historical_rotors.UKW_Bruno, "A", "A")]
    # w = walzensatz(walzen)
    # print(w.enc_string("AAAA"))

    # walzen = [walze(rotors.historical_rotors.al_III, "A", "A"),
    # walze(rotors.historical_rotors.al_II, "A", "A"),
    # walze(rotors.historical_rotors.al_I, "A", "A"),
    # walze(rotors.historical_rotors.al_ETW, "A", "A"),
    # walze(rotors.historical_rotors.al_UKW_B, "A", "A")]
    # w = walzensatz(walzen)
    # # print(w.enc_string("Hello my friend how are you."))
    # print(w.enc_string("17GprdXzojSUreJEqAZaHUIEwWoN"))

    walzen = [walze(rotors.historical_rotors.co_III, "A", "A"),
    walze(rotors.historical_rotors.co_II, "A", "A"),
    walze(rotors.historical_rotors.co_I, "A", "A"),
    walze(rotors.historical_rotors.co_ETW, "A", "A"),
    walze(rotors.historical_rotors.co_UKW_B, "A", "A")]
    w = walzensatz(walzen)
    # print(w.enc_string("Hello my friend, how are you?"))
    print(w.enc_string("maE,7ZIl2qEq3OYwrNNZozPMpQWey"))



# Call the main function at the end of the file
main()