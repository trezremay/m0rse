# Morse Code Screen Flasher and Decoder

This project contains two Python scripts: one to flash Morse code using your screen's brightness and another to decode Morse code using a webcam. The encoder script adjusts the screen's brightness to represent dots and dashes, while the decoder script captures the screen's flashes via a webcam and interprets the Morse code.

## Features

- **Screen Brightness Flasher**: Encodes messages into Morse code by altering screen brightness.
- **Webcam Decoder**: Decodes the Morse code flashes using a webcam and converts them back into text.
- **Cross-Platform**: Compatible with macOS (with specific adjustments) and other platforms.

## Requirements

- **Python 3.6+**
- **Required Python Packages**:
  - `screen-brightness-control` (for brightness control)
  - `opencv-python` (for video capture)
- **macOS-specific**:
  - `brightness` command-line tool (for brightness control)

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/morse-code-flasher.git
   cd morse-code-flasher
