import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, I am unable to connect to the service.")
            return ""

def respond_to_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")
    
    elif "time" in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The time is {now}.")
    
    elif "date" in command:
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        speak(f"Today's date is {today}.")
    
    elif "search" in command:
        speak("What do you want to search for?")
        search_query = recognize_speech()
        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Here are the search results for {search_query}.")
    
    else:
        speak("Sorry, I didn't understand that command.")

def main():
    while True:
        command = recognize_speech()
        if command:
            respond_to_command(command)

if __name__ == "__main__":
    main()
