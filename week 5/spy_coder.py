def spy(S):
    message = input("Enter the message your want to hide:")
    message = message.upper()
    
    print(message)
    alphabet = ["A", "B", "C", "D", "E", "F"," G","H", "I", "J", "K", "L", "M"," N", "O", "P","Q", "R","S", "T", "U", "V","W", "X","Y","Z"]
    
    for letter in message:
        if letter == " ":
            print(end= "")
        else:
            idx = alphabet.index(letter)
            idx_end = (idx + S)%26
            letter_end = alphabet[idx_end]
            
            print(letter_end, end = "")

spy(5)

    


