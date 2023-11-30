from Bard import Chatbot
import speech_recognition as sr
import pyttsx3
import sys
import platform
import json
import os


def load_config():
    CONFIG_KEYS = ['Bard_Secure_1PSID', 'Bard_Secure_1PSIDTS']
    plt = platform.system()
    username = os.getenv('username') if plt == 'Windows' else os.getlogin()
    config_path = os.path.join(os.path.expanduser(f'~{username}'), '.config', 'BardAssistant', 'config.json')

    with open(config_path) as f:
        config = json.load(f)
        return {key: config[key] for key in CONFIG_KEYS}


def initialize_engine():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    return engine

def speak(text):
    engine = initialize_engine()
    cleaned_text = ''.join(char for char in text if char.isalnum() or char.isspace())
    engine.say(cleaned_text)
    engine.runAndWait()

def prompt_bard(prompt):
    CONFIG = load_config()
    chatbot = Chatbot(CONFIG['Bard_Secure_1PSID'], CONFIG['Bard_Secure_1PSIDTS'])
    response = chatbot.ask(prompt)
    return response['content']

def __bard__():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        while True:
            while True:
                try:
                    print("\n say 'google' to wake me up.\n")
                    audio = r.listen(source)
                    result = r.recognize_google(audio)
                    if 'google' in result.lower().strip():
                        break
                    else:
                        print("\nNo wake word found. Try again\n")
                except Exception as e:
                    print("Error: ", e)
                    continue
            
            try:
                print("\nHello There, what you want me to do?\n")
                audio = r.listen(source)
                result = r.recognize_google(audio)
                print(result)
                if len(result.strip()) == 0:
                    print("Empty prompt, speak again")
                    speak("Empty prompt, speak again")
                    continue
            except Exception as e:
                print("Error: ", e)
                continue
            response = prompt_bard(result)
            if sys.platform.startswith('win'):
                print("Bard's respone: ", response)
            else:
                print("\033[1;36m" + "Bard's response: ", response, '\n' + "\033[0m")
            speak(response)

try:
    __bard__()
except KeyboardInterrupt:
    exit(0)
