from rotor import rotor

class historical_rotors:
    # Enigma I
    # Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
    ETW = rotor("ETW", "1930", "Enigma I", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ["A"])
    I = rotor("I", "1930", "Enigma I", "EKMFLGDQVZNTOWYHXUSPAIBRCJ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["Q"])
    II = rotor("II", "1930", "Enigma I", "AJDKSIRUXBLHWTMCQGZNPYFVOE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["E"])
    III = rotor("III", "1930", "Enigma I", "BDFHJLCPRTXVZNYEIWGAKMUSQO", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["V"])
    # M3
    IV = rotor("IV", "15.12.1938", "M3", "ESOVPZJAYQUIRHXLNFTGKDCMWB", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["J"])
    V = rotor("V", "15.12.1938", "M3", "VZBRGITYUPSDNHLXAWMJQOFECK", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["Z"])
    # M3 & M4
    VI = rotor("VI", "1939", "M3 & M4", "JPGVOUMFYQBENHZRDKASXLICTW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["Z", "M"])
    VII = rotor("VII", "1939", "M3 & M4", "NZJHGRCXMYSWBOUFAIVLPEKQDT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["Z", "M"])
    VIII = rotor("VIII", "1939", "M3 & M4", "FKQHTLXOCBJSPDZRAMEWNIUYGV", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ["Z", "M"])
    # M3 and under
    UKW_A = rotor("UKW A", "-", "-", "EJMZALYXVBWFCRQUONTSPIKHGD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ["A"])
    UKW_B = rotor("UKW B", "2.11.1937", "-", "YRUHQSLDPXNGOKMIEBFZCWVJAT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ["A"])
    UKW_C = rotor("UKW C", "1940/1941", "-", "FVPJIAOYEDRZXWGCTKUQSBNMHL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ["A"])
    # M4
    ETW_M4 = rotor("ETW", "-", "M4", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ["A"])
    Beta = rotor("Beta", "1.2.1942", "M4", "LEYJVCNIXWPBQMDRTAKZGFUHOS", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "GRW", ["A"])
    Gamma = rotor("Gamma", "1.7.1943", "M4", "FSOKANUERHMBTIYCWLQPZXVGJD", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "GRW", ["A"])
    UKW_Bruno = rotor("UKW Bruno", "1.2.1942", "M4", "ENKQAUYWJICOPBLMDXZVFTHRGS", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ["A"])
    UKW_Cäsar = rotor("UKW Cäsar", "1.7.1943", "M4", "RDOBJNTKVEHMLFCWZAXGYIPSUQ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ["A"])

    ul_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    # Upper & Lowercase as well as numbers
    ul_ETW = rotor("ETW", "1930", "Enigma I", 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789', ul_alphabet, "ETW", ["A"])
    ul_I = rotor("I", "1930", "Enigma I", 'xmlGHpXMucE9Dnt0LQ8IvU7S5P4yeBTokijaWRrKYbJF3dOwqhZ62zVsfCAgN1', ul_alphabet, "NORMAL", ["Q"])
    ul_II = rotor("II", "1930", "Enigma I", 'EfnlwWs5kzbgRML3jcAJyFVi1xCeDdXqva68pUrBIGoKP7Z9m4u0SNTQ2hHtOY', ul_alphabet, "NORMAL", ["E"])
    ul_III = rotor("III", "1930", "Enigma I", 'aCc0RdH7y6rUg5XjAzKpPm3i8SBOZwustnFV9NkWMbJTGDLoq2hIfel1EY4Qvx', ul_alphabet, "NORMAL", ["V"])
    ul_UKW_A = rotor("UKW A", "-", "-", 'V9lP6reqYWo87vgDd4zt0AJnIwjukQGmOs2acCfXK1HFhTbNZ35SUpixRyEMLB', ul_alphabet, "UKW", ["A"])
    ul_UKW_B = rotor("UKW B", "2.11.1937", "-", 'XPL64bviYt8CNMhBnpzjc3gAI7yFUed2WOHTomlQkR9w1J5Gr0aSxsfVEuDZKq', ul_alphabet, "UKW", ["A"])
    ul_UKW_C = rotor("UKW C", "1940/1941", "-", '5UaZQLJ4jG3FvpcXE6foBYlPVDCiOmuSt0bI1Wd7TN9srgeM2yx8hkwKHARnzq', ul_alphabet, "UKW", ["A"])

    al_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. '
    # Upper & Lowercase as well as numbers
    al_ETW = rotor("ETW", "1930", "Enigma I", 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789. ', al_alphabet, "ETW", ["A"])
    al_I = rotor("I", "1930", "Enigma I", 'aQZ74Suet891msxzDNjwWKIlCAOy ghGHXdbPLFoE0RkcpirT.Mn6f35YVvB2JUq', al_alphabet, "NORMAL", ["Q"])
    al_II = rotor("II", "1930", "Enigma I", 'DSnIX7tTqPzvUY0OM fKHdoba6piFBEs1eN5lr83VhLjcuWG9CAy2m.QJZwR4xkg', al_alphabet, "NORMAL", ["E"])
    al_III = rotor("III", "1930", "Enigma I", 'Kt7f5oVGwHY6ek8cuC1njiEA WyN0TlUdXORpQBxL2qJmDg9Iz.Ma3PvrbsSF4Zh', al_alphabet, "NORMAL", ["V"])
    al_UKW_A = rotor("UKW A", "-", "-", 'hSOuqaRf NvoxJCpWGBygYQ8V6F1sliHUAetmdkzLPE3cjDK2MTn7bwr54Z0X.9I', al_alphabet, "UKW", ["A"])
    al_UKW_B = rotor("UKW B", "2.11.1937", "-", ' IxMfZ2aBycnD3Xtklmwd09O4FHgKUqEb7jiQRSL.vesrP6pTCJ8V5GNY1uhzWoA', al_alphabet, "UKW", ["A"])
    al_UKW_C = rotor("UKW C", "1940/1941", "-", 'M1enYldLQgWHAZcwItUvSxK2ENuyOGCzJ3 4rFsD6.9kmRaTPVbf5BXhj0o87qpi', al_alphabet, "UKW", ["A"])

    co_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,?!: '
    co_wirings = ['YNFf8l92V3c,sQUIK0dOraq:Wx5Pomg?1!LSejHvzGMkbpD6Cu.EXh7Ri nA4JZwtByT',
    '1K6jH5,tWpwn?giR8r0P:z4UTSsbMyFkf7dOeZ3um2cGQ!Co. qaVIlxBXDvLNJEA9Yh',
    'PkKCWrRpAX?B!xEO04:QIcm LMegUF9j32Sy6uv.szoZDqnd7,1JwblfhVTGY5taiHN8',
    'es!6vOcuVg5pd1Fy,t W8IT9.xzfGMAbJklnhi:j3L40BRHE?ZParN7oqKD2UXYQwCmS',
    'G5q0IcAZEslyazTd!7bOpXoV,HMSFP?jur8f6KvtWUChJngm1.LNDw4 2BkRi:xYeQ93',
    'IaTmi5SOArVp?qHfxjGC4K.s:!B7wy,PozER09D6gLNJX8 2cQdhk3v1UFnbtlWeMZYu']
    # Upper & Lowercase as well as numbers
    co_ETW = rotor("ETW", "1930", "Enigma I", co_alphabet, co_alphabet, "ETW", ["A"])
    co_I = rotor("I", "1930", "Enigma I", co_wirings[0], co_alphabet, "NORMAL", ["Q"])
    co_II = rotor("II", "1930", "Enigma I", co_wirings[1], co_alphabet, "NORMAL", ["E"])
    co_III = rotor("III", "1930", "Enigma I", co_wirings[2], co_alphabet, "NORMAL", ["V"])
    co_UKW_A = rotor("UKW A", "-", "-", co_wirings[3], co_alphabet, "UKW", ["A"])
    co_UKW_B = rotor("UKW B", "2.11.1937", "-", co_wirings[4], co_alphabet, "UKW", ["A"])
    co_UKW_C = rotor("UKW C", "1940/1941", "-", co_wirings[5], co_alphabet, "UKW", ["A"])
