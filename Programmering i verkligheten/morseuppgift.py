#morsealfabet

def morse(meddelande): 
    morseAlfabet = [".-", "-...", "-.-.", "-..",".","..-.","--","....","..",".---","-.-",".-..","--","-.","---",".--","--.-",".-.","...","-", "..-","...-",".--","-..-","-.--","--..",".--.-",".-.-","---"]
    alfabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ"
    morseKod = ""


    for bokstav in meddelande:
        # leta rätt på indexet på respektive bokstav
        position = alfabet.index(bokstav)
        morseKod += morseAlfabet[position]

    return morseKod


print(morse("PYTHON"))
