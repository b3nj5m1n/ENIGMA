import rotors
from enigma import ENIGMA

class enigmas:

    class M3:
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
        ENIGMA = ENIGMA(ROTORS, "M3", 5)










