import string
from frequency_table import *
def shift_letter(letter, S, alpha = string.ascii_uppercase):
    letterUp = letter.upper()  # uppercase the letter
    if letterUp in alpha:
        indx = alpha.index(letterUp)  # original index of letter
        indx_end = ( indx - S) % 26  # shifted letter's index
        letter_end = alpha[indx_end]
        return letter_end
    else:
        print("Vaild")

def shift_text(text, S, alpha = string.ascii_uppercase):
    txt_str_result = ""
    for letter in text:
        txt_str_result += shift_letter(letter, S)
    print(txt_str_result)
    print(get_letterGoodness(txt_str_result))



shift_text("hud", 6)

        


