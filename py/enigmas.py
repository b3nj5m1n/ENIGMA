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

    class Enigma_B:
        ROTORS = [
            rotors.historicalrotors.Enigma_B.I, # 0
            rotors.historicalrotors.Enigma_B.II, # 1
            rotors.historicalrotors.Enigma_B.III, # 2
            rotors.historicalrotors.Enigma_B.ETW, # 3
            rotors.historicalrotors.Enigma_B.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Enigma B", 5)

    class Enigma_D:
        ROTORS = [
            rotors.historicalrotors.Enigma_D.I, # 0
            rotors.historicalrotors.Enigma_D.II, # 1
            rotors.historicalrotors.Enigma_D.III, # 2
            rotors.historicalrotors.Enigma_D.ETW, # 3
            rotors.historicalrotors.Enigma_D.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Enigma D", 5)

    class Enigma_K:
        ROTORS = [
            rotors.historicalrotors.Enigma_K.I, # 0
            rotors.historicalrotors.Enigma_K.II, # 1
            rotors.historicalrotors.Enigma_K.III, # 2
            rotors.historicalrotors.Enigma_K.ETW, # 3
            rotors.historicalrotors.Enigma_K.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Enigma K", 5)

    class Enigma_I:
        ROTORS = [
            rotors.historicalrotors.Enigma_I.I, # 0
            rotors.historicalrotors.Enigma_I.II, # 1
            rotors.historicalrotors.Enigma_I.III, # 2
            rotors.historicalrotors.Enigma_I.IV, # 3
            rotors.historicalrotors.Enigma_I.V, # 4
            rotors.historicalrotors.Enigma_I.ETW, # 5
            rotors.historicalrotors.Enigma_I.UKW_A, # 6
            rotors.historicalrotors.Enigma_I.UKW_B, # 7
            rotors.historicalrotors.Enigma_I.UKW_C # 8
        ]
        ENIGMA = ENIGMA(ROTORS, "Enigma I", 5)

    class Norway_Enigma:
        ROTORS = [
            rotors.historicalrotors.Norway_Enigma.I, # 0
            rotors.historicalrotors.Norway_Enigma.II, # 1
            rotors.historicalrotors.Norway_Enigma.III, # 2
            rotors.historicalrotors.Norway_Enigma.IV, # 3
            rotors.historicalrotors.Norway_Enigma.V, # 4
            rotors.historicalrotors.Norway_Enigma.ETW, # 5
            rotors.historicalrotors.Norway_Enigma.UKW, # 6
        ]
        ENIGMA = ENIGMA(ROTORS, "Norway Enigma", 5)

    class Zählwerk_Enigma_A28:
        ROTORS = [
            rotors.historicalrotors.Zählwerk_Enigma_A28.I, # 0
            rotors.historicalrotors.Zählwerk_Enigma_A28.II, # 1
            rotors.historicalrotors.Zählwerk_Enigma_A28.III, # 2
            rotors.historicalrotors.Zählwerk_Enigma_A28.ETW, # 3
            rotors.historicalrotors.Zählwerk_Enigma_A28.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Zählwerk Enigma A28", 5)

    class Enigma_G:
        ROTORS = [
            rotors.historicalrotors.Enigma_G.I, # 0
            rotors.historicalrotors.Enigma_G.II, # 1
            rotors.historicalrotors.Enigma_G.III, # 2
            rotors.historicalrotors.Enigma_G.ETW, # 3
            rotors.historicalrotors.Enigma_G.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Enigma G", 5)

    class Zählwerk_Enigma_GA312:
        ROTORS = [
            rotors.historicalrotors.Zählwerk_Enigma_GA312.I, # 0
            rotors.historicalrotors.Zählwerk_Enigma_GA312.II, # 1
            rotors.historicalrotors.Zählwerk_Enigma_GA312.III, # 2
            rotors.historicalrotors.Zählwerk_Enigma_GA312.ETW, # 3
            rotors.historicalrotors.Zählwerk_Enigma_GA312.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Zählwerk Enigma G A312", 5)

    class Zählwerk_Enigma_GA260:
        ROTORS = [
            rotors.historicalrotors.Zählwerk_Enigma_GA260.I, # 0
            rotors.historicalrotors.Zählwerk_Enigma_GA260.II, # 1
            rotors.historicalrotors.Zählwerk_Enigma_GA260.III, # 2
            rotors.historicalrotors.Zählwerk_Enigma_GA260.ETW, # 3
            rotors.historicalrotors.Zählwerk_Enigma_GA260.UKW, # 4
        ]
        ENIGMA = ENIGMA(ROTORS, "Zählwerk Enigma G A260", 5)

