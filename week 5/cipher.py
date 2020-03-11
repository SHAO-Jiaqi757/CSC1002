# Caeser-cipher (shift-cipher)
# Ref: https://cscircles.cemc.uwaterloo.ca/15c
# 
# Skills: functions, x
# list comprehension, dictionary and sorted 
import string

# Letter frequencies copied from https://cscircles.cemc.uwaterloo.ca/15c
letterGoodness = \
    [0.0817, 0.0149, 0.0278, 0.0425, 0.127, 0.0223, 0.0202, 
    0.0609, 0.0697, 0.0015, 0.0077, 0.0402, 0.0241, 0.0675, 
    0.0751, 0.0193, 0.0009, 0.0599, 0.0633, 0.0906, 0.0276, 
    0.0098, 0.0236, 0.0015, 0.0197, 0.0007]

goodnessByLetter = {}

# shift a single letter
def shift(ch, value, alpha=string.ascii_uppercase):
    if ch in alpha:
        idx = alpha.index(ch)
        pos = (idx + value) % len(alpha)
        return alpha[pos]
    return ch

# shift-cipher a string with given shift value
def shift_cipher(text, value, alpha=string.ascii_uppercase):
    ret = [shift(c, value) for c in text]
    return ''.join(ret)

# compute the goodness value
def goodness_value(text):
    val = [goodnessByLetter.get(c,0) for c in text]
    return sum(val)

# Guess the shift value based on letter frequencies
# by trying all possible shift values (0,1,3,4,..)
def goodness(text, alpha=string.ascii_uppercase):
    values = {}
    for val in range(len(alpha)):
        decode = shift_cipher(text, -val, alpha)
        values[val] = goodness_value(decode)
    ret = sorted(values.keys(), key=lambda x: values[x])
    return ret[-1]
    
if __name__ == "__main__":

    alpha = string.ascii_uppercase
    goodnessByLetter = dict( zip(alpha, letterGoodness) )

    text = "JOIN ME AT EIGHT BY THE ZOO"
    print('\nThe text string to be encoded: "{}"\n'.format(text))

    while True:
        val = input('Enter shift value 0-25 (x to quit):')
        if val == "x":
            break
        try:
            # For demo - skip input validation
            val = int(val) % 26
            encode = shift_cipher(text, val, alpha)
            print("Encoded text:", encode)
            guess = goodness(encode, alpha)
            print('Goodness value :', guess)
            decode = shift_cipher(encode, -guess, alpha)
            print("Decoded text:", decode)
        except:
            print('Error!!!!!')
            continue


