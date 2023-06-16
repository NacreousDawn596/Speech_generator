import pyttsx3
def text_to_speech(text, voice_idx=None, speed=200):
    engine = pyttsx3.init()
    engine.setProperty('voice', engine.getProperty('voices')[voice_idx].id) if voice_idx else engine.setProperty('rate', speed)
    engine.say(text)
    engine.runAndWait()

read_text_from_file = lambda file_path: open(file_path, 'r').read()

prompt_user = lambda: read_text_from_file(input("Enter file path: ")) if input("Enter 'f' to read from file or 't' to read text directly: ") == 'f' else input("Enter text: ")

start_speech_synthesis = lambda: text_to_speech(prompt_user(), int(input("Enter voice index (0-based, press enter for default): ")), int(input("Enter speed (in wpm, press enter for default 200): ")))

if __name__ == '__main__': start_speech_synthesis()
