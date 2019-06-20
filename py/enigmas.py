import rotors
from enigma import ENIGMA

class enigmas:

    class M3:
        ROTORS = [
            rotors.historicalrotors.M3.I, # 0
            rotors.historicalrotors.M3.II, # 1
            rotors.historicalrotors.M3.III, # 2
            rotors.historicalrotors.M3.IV, # 3
            rotors.historicalrotors.M3.V, # 4
            rotors.historicalrotors.M3.VI, # 5
            rotors.historicalrotors.M3.VII, # 6
            rotors.historicalrotors.M3.VIII, # 7
            rotors.historicalrotors.M3.ETW, # 8
            rotors.historicalrotors.M3.UKW_B, # 9
            rotors.historicalrotors.M3.UKW_C # 10
        ]
        ENIGMA = ENIGMA(ROTORS, "M3", 5)

    class M4:
        ROTORS = [
            rotors.historicalrotors.M4.I, # 0
            rotors.historicalrotors.M4.II, # 1
            rotors.historicalrotors.M4.III, # 2
            rotors.historicalrotors.M4.IV, # 3
            rotors.historicalrotors.M4.V, # 4
            rotors.historicalrotors.M4.VI, # 5
            rotors.historicalrotors.M4.VII, # 6
            rotors.historicalrotors.M4.VIII, # 7
            rotors.historicalrotors.M4.Beta, # 8
            rotors.historicalrotors.M4.Gamma, # 9
            rotors.historicalrotors.M4.ETW_M4, # 10
            rotors.historicalrotors.M4.UKW_Bruno, # 11
            rotors.historicalrotors.M4.UKW_Cäsar # 12
        ]
        ENIGMA = ENIGMA(ROTORS, "M4", 5)










