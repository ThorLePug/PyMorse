import json
import time
import winsound

with open('alphabet.json', 'r') as f:
        ALPHABET_DATA = json.load(f)

S_DOT_LENGTH = 0.2 # sec
S_DASH_LENGTH = 3 * S_DOT_LENGTH
ELEMENT_SPACE_LENGTH = S_DOT_LENGTH
LETTER_SPACE_LENGTH = 3 * S_DOT_LENGTH
WORDS_SPACE_LENGTH = 7 * S_DOT_LENGTH
FREQUENCY = 700


def encode(text: str):
    morse_txt = ''
    try:
        for char in text:
            if char != ' ':
                morse_txt += ALPHABET_DATA[char] + ' '
            else:
                morse_txt += '/'
        return morse_txt
    except KeyError:
        print('The text your entered was not valid for morse.')
        return ''


def read_aloud(morse_txt: str):
    for char in morse_txt:
        match char:
            case '.':
                winsound.Beep(FREQUENCY, int(S_DOT_LENGTH * 1000))
            case '-':
                winsound.Beep(FREQUENCY, int(S_DASH_LENGTH * 1000))
            case ' ':
                time.sleep(LETTER_SPACE_LENGTH - 2 * ELEMENT_SPACE_LENGTH)  # -2 to count sleeper before ad after
            case '/':
                time.sleep(WORDS_SPACE_LENGTH - 2 * ELEMENT_SPACE_LENGTH)
        time.sleep(ELEMENT_SPACE_LENGTH)

