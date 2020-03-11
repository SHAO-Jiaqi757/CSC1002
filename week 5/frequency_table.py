table={
"A":.0817,	"B":.0149,	"C":.0278,	"D":.0425,	"E":.1270,	"F":.0223,	"G":.0202,	"H":.0609,	"I":.0697,
"J":.0015,	"K":.0077,	"L":.0402,	"M":.0241,	"N":.0675,	"O":.0751,	"P":.0193,	"Q":.0009,	"R":.0599,
"S":.0633,	"T":.0906,	"U":.0276,	"V":.0098,	"W":.0236,	"X":.0015,	"Y":.0197,	"Z":.0007}

def get_letterGoodness(text):
    goodnessValue = 0
    for letter in text:
        letterGoodness = table[letter]
        goodnessValue += letterGoodness
    return goodnessValue




    