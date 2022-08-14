import morse_engine

if __name__ == "__main__":
    text = input('type text : \n > ')
    morse = morse_engine.encode(text.lower())
    print(morse)
    morse_engine.read_aloud(morse)
