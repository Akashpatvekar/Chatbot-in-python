import os
import webbrowser
import speech_recognition as sr
import pyttsx3

# Text-to-Speech Engine Initialization
engine = pyttsx3.init()

def speak(text):
    """Speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to voice input and return as text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        speak("I'm listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I could not understand.")
            speak("Sorry, I could not understand.")
            return None
        except sr.RequestError:
            print("Speech service is not available.")
            speak("Speech service is not available.")
            return None

def open_website(command):
    """Open a website based on command."""
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "gmail": "https://mail.google.com",
        "spotify": "https://open.spotify.com"
    }
    for site in websites:
        if site in command:
            webbrowser.open(websites[site])
            speak(f"Opening {site}")
            return True
    return False

def open_app(command):
    """Open an application based on command."""
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": "chrome.exe",
        "word": "winword.exe",
        "excel": "excel.exe",
        "spotify": "spotify.exe"
    }
    for app in apps:
        if app in command:
            os.system(f"start {apps[app]}")
            speak(f"Opening {app}")
            return True
    return False

def process_command(command):
    """Process user command and respond."""
    if command is None:
        return

    # Basic responses
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    elif "what is your name" in command:
        speak("I am Alexa, your virtual assistant.")
    elif "how are you" in command:
        speak("I am fine, thank you. How can I assist you?")
    elif "quit" in command or "exit" in command:
        speak("Goodbye! Have a great day.")
        exit()

    # Open website or app
    elif open_website(command):
        pass
    elif open_app(command):
        pass
    else:
        speak("I didn't understand that command. Please try again.")

def main():
    """Main function to run Alexa chatbot."""
    speak("Hello Akash , I am Alexa, your voice assistant.")
    speak("You can ask me to open apps, websites, or have a conversation.")
    while True:
        command = listen()
        process_command(command)

if __name__ == "__main__":
    main()
