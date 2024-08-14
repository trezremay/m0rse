import cv2
import time

# Thresholds for detecting flashes
BRIGHTNESS_THRESHOLD = 200  # This value may need tuning
DOT_THRESHOLD = 0.3
DASH_THRESHOLD = 0.7

def decode_morse_from_video():
    cap = cv2.VideoCapture(0)  # 0 for the default webcam
    last_brightness = None
    morse_code = ""
    start_time = None

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        avg_brightness = gray.mean()

        if last_brightness is None:
            last_brightness = avg_brightness
            continue

        if avg_brightness > BRIGHTNESS_THRESHOLD and last_brightness <= BRIGHTNESS_THRESHOLD:
            start_time = time.time()

        elif avg_brightness <= BRIGHTNESS_THRESHOLD and last_brightness > BRIGHTNESS_THRESHOLD:
            if start_time:
                duration = time.time() - start_time
                if duration < DOT_THRESHOLD:
                    morse_code += "."
                elif duration < DASH_THRESHOLD:
                    morse_code += "-"
                else:
                    # Could be used for adding space between characters
                    morse_code += " "
                start_time = None

        last_brightness = avg_brightness

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return morse_code

def morse_to_text(morse_code):
    inverse_morse_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    text = ""
    for code in morse_code.split(" "):
        if code in inverse_morse_dict:
            text += inverse_morse_dict[code]
        else:
            text += " "  # Add space for unknown codes
    return text

# Example usage:
if __name__ == "__main__":
    morse_code = decode_morse_from_video()
    print(f"Detected Morse Code: {morse_code}")
    print(f"Decoded Text: {morse_to_text(morse_code)}")