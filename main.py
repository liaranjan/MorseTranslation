import pyfiglet as pyfiglet
from morse_code_translator.translator import translate_to_morse
import numpy as np
import simpleaudio as sa
import time

T = "MORSE CODE CONVERTER"
ASCII_art_1 = pyfiglet.figlet_format(T)
print(ASCII_art_1)

def generate_tone(frequency, duration):
    # Number of samples per second
    sample_rate = 44100
    # Generate array with time values
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Generate a tone with the provided frequency and duration
    tone = np.sin(frequency * t * 2 * np.pi)
    # Ensure that highest value is in 16-bit range
    tone *= 32767 / np.max(np.abs(tone))
    # Convert to 16-bit data
    audio_data = tone.astype(np.int16)
    return audio_data

def play_audio(audio):
    play_obj = sa.play_buffer(audio, 1, 2, 44100)
    play_obj.wait_done()

def written(text):
    print(morse_text)

def audio(text):
    morse_text = translate_to_morse(text)
    for symbol in morse_text:
        if symbol == '.':
            audio_data = generate_tone(800, 0.2)
            play_audio(audio_data)
        elif symbol == '-':
            audio_data = generate_tone(800, 0.6)
            play_audio(audio_data)
        elif symbol == ' ':
            time.sleep(0.5)


while True:
    while True:
        try:

            version = input("Would you like your output as print or audio or both? ")
            text = input("Please enter the text to be translated into morse: ")
            morse_text = translate_to_morse(text)

            if version == 'print':
                written(text)
                break
            elif version == 'audio':
                audio(text)
                break
            elif version == 'both':
                written(text)
                audio(text)
                break
            else:
                raise ValueError("Invalid version choice.")
        except Exception as e:
            print(f"There was trouble translating your input. Please check the following and re-enter your input:\n(1) If you entered the correct version choice. \n(2) If you entered correct text - make sure to include only alphanumerics.")
            break

    choice = input("Do you want to translate anything else? (yes/no): ")
    if choice.lower() == "no":
        print("Goodbye!")
        break
    elif choice.lower() != "yes":
        print("Invalid choice. Assuming 'no'. Goodbye!")
        break

