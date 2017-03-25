def alphabet_position(letter): # 65 is capital A
    if (ord(letter) > 64 and ord(letter) < 91):
        return ord(letter)-65
    else:
        return ord(letter)-97

def rotate_character(char,rot):
    if (ord(char) > 64 and ord(char) < 91): # CAPITALIZED
        return chr(((alphabet_position(char) + rot)%26)+65)
    elif (ord(char)<122 and ord(char)>96):
        return chr(((alphabet_position(char) + rot)%26)+97)
    else:
        return char

def encrypt(text, rot):
    encryptedMessage = ""
    for char in text:
        encryptedMessage = encryptedMessage + rotate_character(char, rot)
    return encryptedMessage
