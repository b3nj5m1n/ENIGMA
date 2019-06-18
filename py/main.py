import sys
import rotors
from walze import walze
from walzensatz import walzensatz
# Main function, args varibale will be set to all the arguments supplied, except for the first one because thats just the name of the python file
def main(args=sys.argv[1:]):

    # walzen = [walze(rotors.rotors.III, "A", "A"),
    # walze(rotors.rotors.II, "A", "A"),
    # walze(rotors.rotors.I, "A", "A"),
    # walze(rotors.rotors.ETW, "A", "A"),
    # walze(rotors.rotors.UKW_B, "A", "A")]
    # w = walzensatz(walzen)
    # print(w.enc_string("AAAAA"))

    # walzen = [walze(rotors.rotors.III, "A", "A"),
    # walze(rotors.rotors.II, "A", "A"),
    # walze(rotors.rotors.I, "A", "A"),
    # walze(rotors.rotors.Beta, "A", "A"),
    # walze(rotors.rotors.ETW_M4, "A", "A"),
    # walze(rotors.rotors.UKW_Bruno, "A", "A")]
    # w = walzensatz(walzen)
    # print(w.enc_string("AAAA"))

    # walzen = [walze(rotors.rotors.al_III, "A", "A"),
    # walze(rotors.rotors.al_II, "A", "A"),
    # walze(rotors.rotors.al_I, "A", "A"),
    # walze(rotors.rotors.al_ETW, "A", "A"),
    # walze(rotors.rotors.al_UKW_B, "A", "A")]
    # w = walzensatz(walzen)
    # # print(w.enc_string("Hello my friend how are you."))
    # print(w.enc_string("17GprdXzojSUreJEqAZaHUIEwWoN"))

    walzen = [walze(rotors.rotors.common_symbols.III, "A", "A"),
    walze(rotors.rotors.common_symbols.II, "A", "A"),
    walze(rotors.rotors.common_symbols.I, "A", "A"),
    walze(rotors.rotors.common_symbols.ETW, "A", "A"),
    walze(rotors.rotors.common_symbols.UKW_B, "A", "A")]
    w = walzensatz(walzen)
    # print(w.enc_string("Hello my friend, how are you?"))
    print(w.enc_string("maE,7ZIl2qEq3OYwrNNZozPMpQWey"))



# Call the main function at the end of the file
main()