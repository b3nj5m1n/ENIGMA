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