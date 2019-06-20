import sys
import rotors
from walze import walze
import enigma


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

    ROTORS = [
        rotors.historicalrotors.M3.I,
        rotors.historicalrotors.M3.II,
        rotors.historicalrotors.M3.III,
        rotors.historicalrotors.M3.IV,
        rotors.historicalrotors.M3.V,
        rotors.historicalrotors.M3.VI,
        rotors.historicalrotors.M3.VII,
        rotors.historicalrotors.M3.VIII,
        rotors.historicalrotors.M3.ETW,
        rotors.historicalrotors.M3.UKW_B,
        rotors.historicalrotors.M3.UKW_C
    ]
    # w = walzensatz(walzen) # walzensatz.restore("save.pkl")
    # w.save("save.pkl")

    ENIGMA = enigma.ENIGMA(ROTORS, "M3", 4)
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
        
    ]
    ENIGMA.create_enigma(SETTINGS, WALZEN, STECKBRETT)
    print( ENIGMA.enc_string("AAAAAAAA") )

    # print(w.enc_string("ALANMATHISONTURINGOBEFRSTJRJUNEJUNEWASANENGLISHMATHEMATICIANCOMPUTERSCIENTISTLOGICIANCRYPTANALYSTPHILOSOPHERANDTHEORETICALBIOLOGISTTURINGWASHIGHLYINFLUENTIALINTHEDEVELOPMENTOFTHEORETICALCOMPUTERSCIENCEPROVIDINGAFORMALISATIONOFTHECONCEPTSOFALGORITHMANDCOMPUTATIONWITHTHETURINGMACHINEWHICHCANBECONSIDEREDAMODELOFAGENERALPURPOSECOMPUTERTURINGISWIDELYCONSIDEREDTOBETHEFATHEROFTHEORETICALCOMPUTERSCIENCEANDARTIFICIALINTELLIGENCEDESPITETHESEACCOMPLISHMENTSHEWASNEVERFULLYRECOGNISEDINHISHOMECOUNTRYDURINGHISLIFETIMEDUETOHISHOMOSEXUALITYWHICHWASTHENACRIMEINTHEUK"))
    


# Call the main function at the end of the file
main()