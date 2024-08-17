
import cv2
import time

# Morse code dictionary
MORSE_CODE_DICT = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
    '---..': '8', '----.': '9'
}

def decode_morse(morse_code):
    return ''.join(MORSE_CODE_DICT.get(code, '') for code in morse_code.split(' '))

def capture_and_decode():
    cap = cv2.VideoCapture(0)
    last_brightness = 0
    morse_code = []
    current_symbol = []
    start_time = None

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Calculate brightness
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            brightness = gray.mean()

            if brightness > 100:  # Arbitrary threshold for detecting a flash
                if last_brightness <= 100:
                    start_time = time.time()
            else:
                if last_brightness > 100 and start_time:
                    duration = time.time() - start_time
                    if duration < 0.3:
                        current_symbol.append('.')
                    elif duration < 0.7:
                        current_symbol.append('-')
                    else:
                        if current_symbol:
                            morse_code.append(''.join(current_symbol))
                        current_symbol = []
                
                if len(morse_code) > 0 and len(current_symbol) == 0:
                    decoded_message = decode_morse(' '.join(morse_code))
                    print(f"Decoded Message: {decoded_message}")
                    morse_code = []

            last_brightness = brightness

            # Show the frame (for visual debugging)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_and_decode()