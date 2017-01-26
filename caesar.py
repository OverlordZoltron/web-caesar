def alphabet_position(letter):
    # check if lowercase
    if (ord(letter) >= 97) and (ord(letter) <= 122):
        return ord(letter)-97
    # check if uppercase
    elif (ord(letter) >= 65) and (ord(letter) <= 90):
        return ord(letter)-65
    # if neither, pass over this step
    else:
        pass


def rotate_character(char, rot):
    #check if lowercase
    if (ord(char) >= 97) and (ord(char) <= 122):
        return chr(97+(alphabet_position(char)+rot)%26)
    #check if uppercase
    elif (ord(char) >= 65) and (ord(char) <= 90):
        return chr(65+(alphabet_position(char)+rot)%26)
    #if neither, return the character
    else:
        return char


def encrypt(text, rot):
    #create new string
    new_text = ""
    #for each char in the text
    for char in range(len(text)):
        #rotate that character according to the ROT and put it in the new string
        new_text += rotate_character(text[char], int(rot))
    return new_text