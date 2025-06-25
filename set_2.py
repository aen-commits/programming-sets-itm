# shift_letter (python)
def shift_letter(letter, shift):
    if letter == " ":
        return " "
    index = ord(letter) - ord('A')
    new_index = (index + shift) % 26
    return chr(new_index + ord('A'))

# caesar_cipher (Python)
def caesar_cipher(message, shift):
    result = []

    for char in message:
        if char.isalpha():
            new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
    
    return ''.join(result)

# shift_by_letter (Python)
def shift_by_letter(letter, letter_shift):
    if letter == " ":
        return letter
    shift_value = ord(letter_shift) - ord('A')
    new_letter = chr((ord(letter) - ord('A') + shift_value) % 26 + ord('A'))

    return new_letter

# vigenere_cipher (Python)
def vigenere_cipher(message, key):
    number = 0 
    new_key = ""
    for i in message:
        if i == " ":
            new_key = new_key + " "
            number = number + 1
        else:
            new_key = new_key + key[number % len(key)]
            number = number + 1
    final = ""

    for i in range(len(message)):
        message_letter = message[i]
        key_letter = new_key[i]
        if message_letter == " ":
            final = final + " "
        else:
            shift = (ord(message_letter) - ord('A') + ord(key_letter) - ord('A')) % 26
            final = final + chr(shift + ord('A'))
    return final

# scytale_cipher (Python)
def scytale_cipher(message, shift):
    if len(message) % shift != 0:
        message = message + '_' * (shift - len(message) % shift)
    
    encoded_message = []
    for i in range(len(message)):
        encoded_message.append(message[(i // shift) + (len(message) // shift) * (i % shift)])
    
    return ''.join(encoded_message)

# scytale_decipher (Python)
def scytale_decipher(message, shift):
    num_columns = shift
    num_rows = len(message) // shift

    grid = [''] * num_columns

    index = 0
    for i in range(num_rows):
        for j in range(num_columns):
            grid[j] += message[index]
            index += 1

    decoded_message = ''.join(grid)

    return decoded_message