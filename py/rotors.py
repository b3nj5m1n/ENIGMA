from rotor import rotor

class rotors:
    class uppercase_lowercase_numbers:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        ETW = rotor("ETW", "-", "-", 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', alphabet, "ETW", ["A"])
        I = rotor("I", "-", "-", 'xmlGHpXMucE9Dnt0LQ8IvU7S5P4yeBTokijaWRrKYbJF3dOwqhZ62zVsfCAgN1', alphabet, "NORMAL", ["Q"])
        II = rotor("II", "-", "-", 'EfnlwWs5kzbgRML3jcAJyFVi1xCeDdXqva68pUrBIGoKP7Z9m4u0SNTQ2hHtOY', alphabet, "NORMAL", ["E"])
        III = rotor("III", "-", "-", 'aCc0RdH7y6rUg5XjAzKpPm3i8SBOZwustnFV9NkWMbJTGDLoq2hIfel1EY4Qvx', alphabet, "NORMAL", ["V"])
        UKW_A = rotor("UKW A", "-", "-", 'V9lP6reqYWo87vgDd4zt0AJnIwjukQGmOs2acCfXK1HFhTbNZ35SUpixRyEMLB', alphabet, "UKW", ["A"])
        UKW_B = rotor("UKW B", "-", "-", 'XPL64bviYt8CNMhBnpzjc3gAI7yFUed2WOHTomlQkR9w1J5Gr0aSxsfVEuDZKq', alphabet, "UKW", ["A"])
        UKW_C = rotor("UKW C", "-", "-", '5UaZQLJ4jG3FvpcXE6foBYlPVDCiOmuSt0bI1Wd7TN9srgeM2yx8hkwKHARnzq', alphabet, "UKW", ["A"])
    class uppercase_lowercase_numbers_spaces_dot:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. '
        ETW = rotor("ETW", "-", "-", 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. ', alphabet, "ETW", ["A"])
        I = rotor("I", "-", "-", 'aQZ74Suet891msxzDNjwWKIlCAOy ghGHXdbPLFoE0RkcpirT.Mn6f35YVvB2JUq', alphabet, "NORMAL", ["Q"])
        II = rotor("II", "-", "-", 'DSnIX7tTqPzvUY0OM fKHdoba6piFBEs1eN5lr83VhLjcuWG9CAy2m.QJZwR4xkg', alphabet, "NORMAL", ["E"])
        III = rotor("III", "-", "-", 'Kt7f5oVGwHY6ek8cuC1njiEA WyN0TlUdXORpQBxL2qJmDg9Iz.Ma3PvrbsSF4Zh', alphabet, "NORMAL", ["V"])
        UKW_A = rotor("UKW A", "-", "-", 'hSOuqaRf NvoxJCpWGBygYQ8V6F1sliHUAetmdkzLPE3cjDK2MTn7bwr54Z0X.9I', alphabet, "UKW", ["A"])
        UKW_B = rotor("UKW B", "-", "-", ' IxMfZ2aBycnD3Xtklmwd09O4FHgKUqEb7jiQRSL.vesrP6pTCJ8V5GNY1uhzWoA', alphabet, "UKW", ["A"])
        UKW_C = rotor("UKW C", "-", "-", 'M1enYldLQgWHAZcwItUvSxK2ENuyOGCzJ3 4rFsD6.9kmRaTPVbf5BXhj0o87qpi', alphabet, "UKW", ["A"])
    class common_symbols:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,?!: '
        wirings = ['YNFf8l92V3c,sQUIK0dOraq:Wx5Pomg?1!LSejHvzGMkbpD6Cu.EXh7Ri nA4JZwtByT',
        '1K6jH5,tWpwn?giR8r0P:z4UTSsbMyFkf7dOeZ3um2cGQ!Co. qaVIlxBXDvLNJEA9Yh',
        'PkKCWrRpAX?B!xEO04:QIcm LMegUF9j32Sy6uv.szoZDqnd7,1JwblfhVTGY5taiHN8',
        'es!6vOcuVg5pd1Fy,t W8IT9.xzfGMAbJklnhi:j3L40BRHE?ZParN7oqKD2UXYQwCmS',
        'G5q0IcAZEslyazTd!7bOpXoV,HMSFP?jur8f6KvtWUChJngm1.LNDw4 2BkRi:xYeQ93',
        'IaTmi5SOArVp?qHfxjGC4K.s:!B7wy,PozER09D6gLNJX8 2cQdhk3v1UFnbtlWeMZYu']
        # Upper & Lowercase as well as numbers
        ETW = rotor("ETW", "-", "-", alphabet, alphabet, "ETW", ["A"])
        I = rotor("I", "-", "-", wirings[0], alphabet, "NORMAL", ["Q"])
        II = rotor("II", "-", "-", wirings[1], alphabet, "NORMAL", ["E"])
        III = rotor("III", "-", "-", wirings[2], alphabet, "NORMAL", ["V"])
        UKW_A = rotor("UKW A", "-", "-", wirings[3], alphabet, "UKW", ["A"])
        UKW_B = rotor("UKW B", "-", "-", wirings[4], alphabet, "UKW", ["A"])
        UKW_C = rotor("UKW C", "-", "-", wirings[5], alphabet, "UKW", ["A"])


class historicalrotors:
    # Most common Enigma in the German army
    class M3:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ETW = rotor("ETW", "1930", "Enigma I", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", alphabet, "ETW", ["A"])
        I = rotor("I", "1930", "Enigma I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", alphabet, "NORMAL", ["Q"])
        II = rotor("II", "1930", "Enigma I", "AJDKSIRUXBLHWTMCQGZNPYFVOE", alphabet, "NORMAL", ["E"])
        III = rotor("III", "1930", "Enigma I", "BDFHJLCPRTXVZNYEIWGAKMUSQO", alphabet, "NORMAL", ["V"])
        IV = rotor("IV", "15.12.1938", "M3", "ESOVPZJAYQUIRHXLNFTGKDCMWB", alphabet, "NORMAL", ["J"])
        V = rotor("V", "15.12.1938", "M3", "VZBRGITYUPSDNHLXAWMJQOFECK", alphabet, "NORMAL", ["Z"])
        VI = rotor("VI", "1939", "M3 & M4", "JPGVOUMFYQBENHZRDKASXLICTW", alphabet, "NORMAL", ["Z", "M"])
        VII = rotor("VII", "1939", "M3 & M4", "NZJHGRCXMYSWBOUFAIVLPEKQDT", alphabet, "NORMAL", ["Z", "M"])
        VIII = rotor("VIII", "1939", "M3 & M4", "FKQHTLXOCBJSPDZRAMEWNIUYGV", alphabet, "NORMAL", ["Z", "M"])
        UKW_B = rotor("UKW B", "2.11.1937", "-", "YRUHQSLDPXNGOKMIEBFZCWVJAT", alphabet, "UKW", ["A"])
        UKW_C = rotor("UKW C", "1940/1941", "-", "FVPJIAOYEDRZXWGCTKUQSBNMHL", alphabet, "UKW", ["A"])
    # Only available to the Navy; Codename: "SHARK"
    class M4:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        ETW_M4 = rotor("ETW", "-", "M4", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", alphabet, "ETW", ["A"])
        I = rotor("I", "1930", "Enigma I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", alphabet, "NORMAL", ["Q"])
        II = rotor("II", "1930", "Enigma I", "AJDKSIRUXBLHWTMCQGZNPYFVOE", alphabet, "NORMAL", ["E"])
        III = rotor("III", "1930", "Enigma I", "BDFHJLCPRTXVZNYEIWGAKMUSQO", alphabet, "NORMAL", ["V"])
        IV = rotor("IV", "15.12.1938", "M3", "ESOVPZJAYQUIRHXLNFTGKDCMWB", alphabet, "NORMAL", ["J"])
        V = rotor("V", "15.12.1938", "M3", "VZBRGITYUPSDNHLXAWMJQOFECK", alphabet, "NORMAL", ["Z"])
        VI = rotor("VI", "1939", "M3 & M4", "JPGVOUMFYQBENHZRDKASXLICTW", alphabet, "NORMAL", ["Z", "M"])
        VII = rotor("VII", "1939", "M3 & M4", "NZJHGRCXMYSWBOUFAIVLPEKQDT", alphabet, "NORMAL", ["Z", "M"])
        VIII = rotor("VIII", "1939", "M3 & M4", "FKQHTLXOCBJSPDZRAMEWNIUYGV", alphabet, "NORMAL", ["Z", "M"])
        Beta = rotor("Beta", "1.2.1942", "M4", "LEYJVCNIXWPBQMDRTAKZGFUHOS", alphabet, "GRW", ["A"])
        Gamma = rotor("Gamma", "1.7.1943", "M4", "FSOKANUERHMBTIYCWLQPZXVGJD", alphabet, "GRW", ["A"])
        UKW_Bruno = rotor("UKW Bruno", "1.2.1942", "M4", "ENKQAUYWJICOPBLMDXZVFTHRGS", alphabet, "UKW", ["A"])
        UKW_Cäsar = rotor("UKW Cäsar", "1.7.1943", "M4", "RDOBJNTKVEHMLFCWZAXGYIPSUQ", alphabet, "UKW", ["A"])
    class Enigma_B:
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ"
        ETW = rotor("ETW", "-", "Enigma B", "ABCDEFGHIJKLMNOPQRSTUVXYZÅÄÖ", alphabet, "ETW", ['A'])
        I = rotor("I", "-", "Enigma B", "PSBGÖXQJDHOÄUCFRTEZVÅINLYMKA", alphabet, "NORMAL", ['Ä'])
        II = rotor("II", "-", "Enigma B", "CHNSYÖADMOTRZXBÄIGÅEKQUPFLVJ", alphabet, "NORMAL", ['Ä'])
        III = rotor("III", "-", "Enigma B", "ÅVQIAÄXRJBÖZSPCFYUNTHDOMEKGL", alphabet, "NORMAL", ['Ä'])
        UKW = rotor("UKW", "-", "Enigma B", "LDGBÄNCPSKJAVFZHXUIÅRMQÖOTEY", alphabet, "UKW", ['A'])
    class Enigma_D:
        ETW = rotor("ETW", "-", "Enigma D", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma D", "LPGSZMHAEOQKVXRFYBUTNICJDW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y'])
        II = rotor("II", "-", "Enigma D", "SLVGBTFXJQOHEWIRZYAMKPCNDU", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Enigma D", "CJGDPSHKTURAWZXFMYNQOBVLIE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['N'])
        UKW = rotor("UKW", "-", "Enigma D", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_K:
        ETW = rotor("ETW", "-", "Enigma K", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma K", "LPGSZMHAEOQKVXRFYBUTNICJDW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y'])
        II = rotor("II", "-", "Enigma K", "SLVGBTFXJQOHEWIRZYAMKPCNDU", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Enigma K", "CJGDPSHKTURAWZXFMYNQOBVLIE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['N'])
        UKW = rotor("UKW", "-", "Enigma K", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_I:
        ETW = rotor("ETW", "-", "Enigma I", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Q'])
        II = rotor("II", "-", "Enigma I", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Enigma I", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['V'])
        IV = rotor("IV", "-", "Enigma I", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['J'])
        V = rotor("V", "-", "Enigma I", "VZBRGITYUPSDNHLXAWMJQOFECK", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Z'])
        UKW_A  = rotor("UKW_A", "-", "Enigma I", "EJMZALYXVBWFCRQUONTSPIKHGD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
        UKW_B = rotor("UKW_B", "-", "Enigma I", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
        UKW_C = rotor("UKW_C", "-", "Enigma I", "FVPJIAOYEDRZXWGCTKUQSBNMHL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Norway_Enigma:
        ETW = rotor("ETW", "-", "Norway Enigma (Enigma I variant)", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Norway Enigma (Enigma I variant)", "WTOKASUYVRBXJHQCPZEFMDINLG", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Q'])
        II = rotor("II", "-", "Norway Enigma (Enigma I variant)", "GJLPUBSWEMCTQVHXAOFZDRKYNI", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Norway Enigma (Enigma I variant)", "JWFMHNBPUSDYTIXVZGRQLAOEKC", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['V'])
        IV = rotor("IV", "-", "Norway Enigma (Enigma I variant)", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['J'])
        V = rotor("V", "-", "Norway Enigma (Enigma I variant)", "HEJXQOTZBVFDASCILWPGYNMURK", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Z'])
        UKW  = rotor("UKW", "-", "Norway Enigma (Enigma I variant)", "MOWJYPUXNDSRAIBFVLKZGQCHET", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Zählwerk_Enigma_A28:
        ETW = rotor("ETW", "-", "Zählwerk Enigma A28", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Zählwerk Enigma A28", "LPGSZMHAEOQKVXRFYBUTNICJDW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'U', 'V', 'W', 'Z', 'A', 'B', 'C', 'E', 'F', 'G', 'I', 'K', 'L', 'O', 'P', 'Q'])
        II = rotor("II", "-", "Zählwerk Enigma A28", "SLVGBTFXJQOHEWIRZYAMKPCNDU", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'T', 'V', 'Y', 'Z', 'A', 'C', 'D', 'F', 'G', 'H', 'K', 'M', 'N', 'Q'])
        III = rotor("III", "-", "Zählwerk Enigma A28", "CJGDPSHKTURAWZXFMYNQOBVLIE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['U', 'W', 'X', 'A', 'E', 'F', 'H', 'K', 'M', 'N', 'R'])
        UKW = rotor("UKW", "-", "Zählwerk Enigma A28", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_G:
        ETW = rotor("ETW", "-", "Zählwerk Enigma (Enigma G)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Zählwerk Enigma (Enigma G)", "LPGSZMHAEOQKVXRFYBUTNICJDW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'U', 'V', 'W', 'Z', 'A', 'B', 'C', 'E', 'F', 'G', 'I', 'K', 'L', 'O', 'P', 'Q'])
        II = rotor("II", "-", "Zählwerk Enigma (Enigma G)", "SLVGBTFXJQOHEWIRZYAMKPCNDU", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'T', 'V', 'Y', 'Z', 'A', 'C', 'D', 'F', 'G', 'H', 'K', 'M', 'N', 'Q'])
        III = rotor("III", "-", "Zählwerk Enigma (Enigma G)", "CJGDPSHKTURAWZXFMYNQOBVLIE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['U', 'W', 'X', 'A', 'E', 'F', 'H', 'K', 'M', 'N', 'R'])
        UKW = rotor("UKW", "-", "Zählwerk Enigma (Enigma G)", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Zählwerk_Enigma_GA312:
        ETW = rotor("ETW", "-", "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)", "DMTWSILRUYQNKFEJCAZBPGXOHV", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'U', 'V', 'W', 'Z', 'A', 'B', 'C', 'E', 'F', 'G', 'I', 'K', 'L', 'O', 'P', 'Q'])
        II = rotor("II", "-", "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)", "HQZGPJTMOBLNCIFDYAWVEUSRKX", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'T', 'V', 'Y', 'Z', 'A', 'C', 'D', 'F', 'G', 'H', 'K', 'M', 'N', 'Q'])
        III = rotor("III", "-", "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)", "UQNTLSZFMREHDPXKIBVYGJCWOA", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['U', 'W', 'X', 'A', 'E', 'F', 'H', 'K', 'M', 'N', 'R'])
        UKW = rotor("UKW", "-", "Zählwerk Enigma (Enigma GA312 | Abwehr Enigma)", "RULQMZJSYGOCETKWDAHNBXPVIF", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Zählwerk_Enigma_GA260:
        ETW = rotor("ETW", "-", "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)", "RCSPBLKQAUMHWYTIFZVGOJNEXD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'U', 'V', 'W', 'Z', 'A', 'B', 'C', 'E', 'F', 'G', 'I', 'K', 'L', 'O', 'P', 'Q'])
        II = rotor("II", "-", "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)", "WCMIBVPJXAROSGNDLZKEYHUFQT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'T', 'V', 'Y', 'Z', 'A', 'C', 'D', 'F', 'G', 'H', 'K', 'M', 'N', 'Q'])
        III = rotor("III", "-", "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)", "FVDHZELSQMAXOKYIWPGCBUJTNR", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['U', 'W', 'X', 'A', 'E', 'F', 'H', 'K', 'M', 'N', 'R'])
        UKW = rotor("UKW", "-", "Zählwerk Enigma (Enigma GA260 | Sicherheitsdienst Enigma)", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Zählwerk_Enigma_GA111:
        ETW = rotor("ETW", "-", "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)", "WLRHBQUNDKJCZSEXOTMAGYFPVI", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'U', 'V', 'W', 'Z', 'A', 'B', 'C', 'E', 'F', 'G', 'I', 'K', 'L', 'O', 'P', 'Q'])
        II = rotor("II", "-", "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)", "TFJQAZWMHLCUIXRDYGOEVBNSKP", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'T', 'V', 'Y', 'Z', 'A', 'C', 'D', 'F', 'G', 'H', 'K', 'M', 'N', 'Q'])
        III = rotor("V", "-", "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)", "QTPIXWVDFRMUSLJOHCANEZKYBG", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['S', 'W', 'Z', 'F', 'H', 'M', 'Q'])
        UKW = rotor("UKW", "-", "Zählwerk Enigma (Enigma GA111 | Hungarian Army Enigma)", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])





