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

    walzen = [walze(rotors.historicalrotors.M3.III, "A", "M"),
    walze(rotors.historicalrotors.M3.V, "A", "C"),
    walze(rotors.historicalrotors.M3.VIII, "A", "Q"),
    walze(rotors.historicalrotors.M3.ETW, "A", "A"),
    walze(rotors.historicalrotors.M3.UKW_B, "A", "A")]
    w = walzensatz(walzen) # walzensatz.restore("save.pkl")
    # w.save("save.pkl")
    print(w.enc_string("ALANMATHISONTURINGOBEFRSTJRJUNEJUNEWASANENGLISHMATHEMATICIANCOMPUTERSCIENTISTLOGICIANCRYPTANALYSTPHILOSOPHERANDTHEORETICALBIOLOGISTTURINGWASHIGHLYINFLUENTIALINTHEDEVELOPMENTOFTHEORETICALCOMPUTERSCIENCEPROVIDINGAFORMALISATIONOFTHECONCEPTSOFALGORITHMANDCOMPUTATIONWITHTHETURINGMACHINEWHICHCANBECONSIDEREDAMODELOFAGENERALPURPOSECOMPUTERTURINGISWIDELYCONSIDEREDTOBETHEFATHEROFTHEORETICALCOMPUTERSCIENCEANDARTIFICIALINTELLIGENCEDESPITETHESEACCOMPLISHMENTSHEWASNEVERFULLYRECOGNISEDINHISHOMECOUNTRYDURINGHISLIFETIMEDUETOHISHOMOSEXUALITYWHICHWASTHENACRIMEINTHEUK"))
    


# Call the main function at the end of the file
main()