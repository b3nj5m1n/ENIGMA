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
    class Modernized:
        alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÖÄÜabcdefghijklmnopqrstuvwxyzöäü0123456789.,:;-_ß!§$&/()=? +*~<>^|'
        wirings = ['N,ä§:Fs0aqEZ(üöxbe&Ä<S8g+K95L^YÖ_32vzc?I$MGdJotWTi.7h >=y)BQmßC6AjP1/lXuÜrV4O|wU~RD*-k;!pnfH',
'Äni_r4yuÜQöY/mk!;^üXß&LpZ>(ScxD:eFB-vfal)KqC.2Iw?ohP ,<O8R1tbEA3*UVGd$=0j+9§g5säzNÖ|~76WMJTH',
'$I(L*4|fP1§AFüßJjD9lnB6Qm;cr<CÄg!XU7RT2Mi3=-kKuqNp0ZE~:bO?ÜHSGw/_&)Öx>.Vä+Yoaevsdöz,^ ht5W8y',
'AQÖJCßzx6Fr^v§q<(.ÄG;ajgY0d2?n>9RT)8Oü*öl+bUÜV3W$:äfHK/XIpDNsM-_ZLthy!=e,mw4oi5uc7~ |&PEk1SB',
'Ö8_~Qs^+(m<)ca$i45fVH9h;Kne?37.|LIrvpxoüZYC,JyFRßö1uOwlGT*:Uj§gÄD btWASzÜ2B!E/&=6äMqd0>PXNk-',
'?&4Ö5M=mxTZhbVDoYiB9>Cvq$(Akä8waJX0eÜ2H!E3üdyIjS*O~N1lLWöK^tÄ,ß;ru:/.6Q-+_RFz|p<PGf§g)cUs 7n',
'$p§x=yePrgfä7AIM9i.l!NHßLUJzÜ;KDV:/üQZjÖdkbY|~-2hRSF<)5Xq*Gtm6,oEaövCBnÄ_^&0O8>3T s1c4w?+u(W',
'82QY X:nUI3|5~&cAL+JZÜ<)41dvb7eßrs-9/GN_ByqPz$oV0FfmhäÖi^.=Ä(ET;ujHk!,MWw?ö6Dül>ORpK*tCS§axg',
'Pp;IJ3WVDE7N&LßA)zlyüHGc9nÄÖöm-X§8=+<5r6SaZxBäj,^~?0oTRÜqUw/*F:ikKeY$s4Cb(O d.M1_Qfv!g2uh|t>',
'!H_ö;4^BÖpYuxÄSc23O15ßa6KeINsWgP?Z|bih-y):+*J(vÜwLrtMkäDz0üTQRFUX,&>§7mEjCVA.<8~ql d=no/$9Gf',
'GnUkWVA27~Sw§q+9ebK^CFE| 6)ÜÄ/Ry1Qs?*,rD(üB<:Njf>=ßLzcx_8m-dH!;$ZIäP&ip40öv3M5.alÖugYOhJotTX']
        ETW = rotor("ETW", "-", "-", alphabet, alphabet, "ETW", ["A"])
        I = rotor("I", "-", "-", wirings[0], alphabet, "NORMAL", ["Q"])
        II = rotor("II", "-", "-", wirings[1], alphabet, "NORMAL", ["E"])
        III = rotor("III", "-", "-", wirings[2], alphabet, "NORMAL", ["V"])
        IV = rotor("IV", "-", "-", wirings[3], alphabet, "NORMAL", ["V"])
        V = rotor("V", "-", "-", wirings[4], alphabet, "NORMAL", ["V"])
        VI = rotor("VI", "-", "-", wirings[5], alphabet, "NORMAL", ["V"])
        VII = rotor("VII", "-", "-", wirings[6], alphabet, "NORMAL", ["V"])
        VIII = rotor("VIII", "-", "-", wirings[7], alphabet, "NORMAL", ["V"])
        UKW_A = rotor("UKW A", "-", "-", wirings[8], alphabet, "UKW", ["A"])
        UKW_B = rotor("UKW B", "-", "-", wirings[9], alphabet, "UKW", ["A"])
        UKW_C = rotor("UKW C", "-", "-", wirings[10], alphabet, "UKW", ["A"])


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
    class Enigma_T:
        ETW = rotor("ETW", "-", "Enigma T (Tirpitz)", "KZROUQHYAIGBLWVSTDXFPNMCJE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma T (Tirpitz)", "KPTYUELOCVGRFQDANJMBSWHZXI", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['W', 'Z', 'E', 'K', 'Q'])
        II = rotor("II", "-", "Enigma T (Tirpitz)", "UPHZLWEQMTDJXCAKSOIGVBYFNR", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['W', 'Z', 'F', 'L', 'R'])
        III = rotor("III", "-", "Enigma T (Tirpitz)", "QUDLYRFEKONVZAXWHMGPJBSICT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['W', 'Z', 'E', 'K', 'Q'])
        IV = rotor("IV", "-", "Enigma T (Tirpitz)", "CIWTBKXNRESPFLYDAGVHQUOJZM", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['W', 'Z', 'F', 'L', 'R'])
        V = rotor("V", "-", "Enigma T (Tirpitz)", "UAXGISNJBVERDYLFZWTPCKOHMQ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y', 'C', 'F', 'K', 'R'])
        VI = rotor("VI", "-", "Enigma T (Tirpitz)", "XFUZGALVHCNYSEWQTDMRBKPIOJ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['X', 'E', 'I', 'M', 'Q'])
        VII = rotor("VII", "-", "Enigma T (Tirpitz)", "BJVFTXPLNAYOZIKWGDQERUCHSM", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y', 'C', 'F', 'K', 'R'])
        VIII = rotor("VIII", "-", "Enigma T (Tirpitz)", "YMTPNZHWKODAJXELUQVGCBISFR", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['X', 'E', 'I', 'M', 'Q'])
        UKW = rotor("UKW", "-", "Enigma T (Tirpitz)", "GEKPBTAUMOCNILJDXZYFHWVQSR", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_K_Commercial:
        ETW = rotor("ETW", "-", "Enigma K (Swiss Commercial)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma K (Swiss Commercial)", "LPGSZMHAEOQKVXRFYBUTNICJDW", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y'])
        II = rotor("II", "-", "Enigma K (Swiss Commercial)", "SLVGBTFXJQOHEWIRZYAMKPCNDU", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Enigma K (Swiss Commercial)", "CJGDPSHKTURAWZXFMYNQOBVLIE", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['N'])
        UKW = rotor("UKW", "-", "Enigma K (Swiss Commercial)", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_K_Swiss_Air_Force:
        ETW = rotor("ETW", "-", "Enigma K (Swiss Air Force)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma K (Swiss Air Force)", "PEZUOHXSCVFMTBGLRINQJWAYDK", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y'])
        II = rotor("II", "-", "Enigma K (Swiss Air Force)", "ZOUESYDKFWPCIQXHMVBLGNJRAT", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Enigma K (Swiss Air Force)", "EHRVXGAOBQUSIMZFLYNWKTPDJC", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['N'])
        UKW = rotor("UKW", "-", "Enigma K (Swiss Air Force)", "IMETCGFRAYSQBZXWLHKDVUPOJN", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_Railyway:
        ETW = rotor("ETW", "-", "Enigma Railway (Rocket)", "QWERTZUIOASDFGHJKPYXCVBNML", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "ETW", ['A'])
        I = rotor("I", "-", "Enigma Railway (Rocket)", "JGDQOXUSCAMIFRVTPNEWKBLZYH", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['Y'])
        II = rotor("II", "-", "Enigma Railway (Rocket)", "NTZPSFBOKMWRCJDIVLAEYUXHGQ", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['E'])
        III = rotor("III", "-", "Enigma Railway (Rocket)", "JVIUBHTCDYAKEQZPOSGXNRMWFL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "NORMAL", ['N'])
        UKW = rotor("UKW", "-", "Enigma Railway (Rocket)", "QYHOGNECVPUZTFDJAXWMKISRBL", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "UKW", ['A'])
    class Enigma_Z:
        ETW = rotor("ETW", "-", "Enigma Z", "1234567890", "1234567890", "ETW", ['1'])
        I = rotor("I", "-", "Enigma Z", "6418270359", "1234567890", "NORMAL", ['9'])
        II = rotor("II", "-", "Enigma Z", "5841097632", "1234567890", "NORMAL", ['9'])
        III = rotor("III", "-", "Enigma Z", "3581620794", "1234567890", "NORMAL", ['9'])
        UKW = rotor("UKW", "-", "Enigma Z", "5079183642", "1234567890", "UKW", ['1'])