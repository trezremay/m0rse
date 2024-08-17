import time
import os

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def set_brightness(level):
    # Ensure a space between the command and its argument
    brightness_level = level / 100.0
    os.system(f"brightness {brightness_level}")

def flash_morse_code(message):
    for char in message.upper():
        if char in MORSE_CODE_DICT:
            morse_code = MORSE_CODE_DICT[char]
            for symbol in morse_code:
                if symbol == '.':
                    set_brightness(100)  # Flash for dot (brightest)
                    time.sleep(0.2)      # Duration for dot
                elif symbol == '-':
                    set_brightness(100)  # Flash for dash (brightest)
                    time.sleep(0.6)      # Duration for dash
                set_brightness(0)       # Turn off flash (darkest)
                time.sleep(0.2)         # Time between symbols
            time.sleep(0.6)             # Time between characters
        elif char == ' ':
            time.sleep(1.2)             # Time between words

# Example usage:
if __name__ == "__main__":
    message = "morning"
    flash_morse_code(message)