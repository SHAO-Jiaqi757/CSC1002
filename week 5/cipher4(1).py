# Caeser-cipher (shift-cipher)
# Ref: https://cscircles.cemc.uwaterloo.ca/15c
# ord() returns the ascii value of a character
# chr() returns the character given the ascii value

# Letter frequencies copied from https://cscircles.cemc.uwaterloo.ca/15c
letterGoodness = \
    [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 
    0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 
    0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 
    0.0098, 0.0236, 0.0015, 0.0197, 0.0007]


# Shift single letter (uppercase) given the character "ch"
# and shift value "value"
def shift(ch, value):
    if ch.isupper():
        val = ord(ch) + value
        if val > ord('Z'):
            val -= 26
        elif val < ord('A'):
            val += 26
        return chr(val)
    return ch

# shift-cipher implementation
# "text" is the string to encode given shift value "value"
def shift_cipher(text, value):
    encode = ""
    for c in text:
        encode += shift(c, value)
    return encode

# Return the goodness value of the given
# "text" based on letter frequencies
def goodness_value(text):
    val = 0
    for c in text:
        if c.isupper():
            idx = ord(c) - ord('A')
            val += letterGoodness[idx]
    return val

# Given the encoded "text" trying
# to guess the shift value based on letter frequencies
# by trying brute force mananer of all possible shift values (0,1,3,4,..)
def goodness(text):
    values = []
    for v in range(26):
        decode = shift_cipher(text, -v)
        values.append( goodness_value(decode) )
    mx = max(values)
    return values.index(mx)
    

if __name__ == "__main__":
    text = "JOIN ME AT EIGHT BY THE ZOO"
    print('\nThe text string to be encoded: "{}"\n'.format(text))
    while True:
        val = input('Enter shift value 0-25 (x to quit):')
        if val == "x":
            break
        try:
            # For demo - skip input validation
            val = int(val) % 26
            encode = shift_cipher(text,val)
            print("Encoded text:", encode)
            guess = goodness(encode)
            print('Goodness value :', guess)
            decode = shift_cipher(encode,-guess)
            print("Decoded text:", decode)
        except:
            print('Error!!!!!')
            continue



        