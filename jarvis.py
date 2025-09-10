import pyttsx3
import speech_recognition as sr
import datetime
import time

# initial
engine = pyttsx3.init()
recognizer = sr.Recognizer()

def speak(text):
    """Make Jarvis Speak"""
    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)

def take_command():
    """Listening to user voice and return as text"""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            command = recognizer.recognize_google(audio).lower()
            print(f"Bos said: {command}")
            return command
    except sr.WaitTimeoutError:
        speak("I didn't hear anything. Please try again.")
        return ""
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand. Please try again.")
        return ""
    
# Main loop
if __name__ == "__main__":
    time.sleep(1)
    
    speak("Hello, I am Jarvis. How can I assist you sir?")

    while True:
        command = take_command()

        if 'hello' in command:
            speak("Hai sir! How are you?")
        elif 'how are you' in command:
            speak("Im good sir! What can I do for you?")
        elif 'time' in command:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")
        elif 'date' in command:
            current_date = datetime.datetime.now().strftime("%B %d, %Y")
            speak(f"Today's date is {current_date}")
        elif 'exit' in command or 'quit' in command or 'stop' in command:
            speak("Goodbye sir! Have a great day.")
            break

        else:
            speak("I didn't catch that sir. Please say it again.")