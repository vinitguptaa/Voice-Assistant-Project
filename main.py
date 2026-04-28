import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import wikipedia
import nltk
from nltk.tokenize import word_tokenize
import musicLibrary

# Download tokenizer once
nltk.download('punkt')

# Initialize recognizer and voice engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Improve voice settings
engine.setProperty("rate", 170)  # speaking speed
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # male voice


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


# NLP-based intent detection
def getIntent(command):
    tokens = word_tokenize(command.lower())

    if "google" in tokens and "search" not in tokens:
        return "open_google"

    elif "youtube" in tokens:
        return "open_youtube"

    elif "github" in tokens:
        return "open_github"

    elif "linkedin" in tokens:
        return "open_linkedin"

    elif "gmail" in tokens:
        return "open_gmail"

    elif "chatgpt" in tokens:
        return "open_chatgpt"

    elif "time" in tokens:
        return "tell_time"

    elif "play" in tokens:
        return "play_music"

    elif "wikipedia" in tokens:
        return "search_wikipedia"

    elif "search" in tokens and "google" in tokens:
        return "search_google"

    elif "exit" in tokens or "stop" in tokens:
        return "exit"

    else:
        return "unknown"


def processCommand(c):
    intent = getIntent(c)
    c = c.lower()

    if intent == "open_google":
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif intent == "open_youtube":
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif intent == "open_github":
        webbrowser.open("https://github.com")
        speak("Opening GitHub")

    elif intent == "open_linkedin":
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn")

    elif intent == "open_gmail":
        webbrowser.open("https://mail.google.com")
        speak("Opening Gmail")

    elif intent == "open_chatgpt":
        webbrowser.open("https://chat.openai.com")
        speak("Opening ChatGPT")

    elif intent == "tell_time":
        current_time = datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "who are you" in c:
        speak("I am Jarvis, your personal voice assistant created using Python with NLP support.")

    elif intent == "play_music":
        words = c.split()

        if len(words) > 1:
            song = words[-1]

            if song in musicLibrary.music:
                link = musicLibrary.music[song]
                webbrowser.open(link)
                speak(f"Playing {song}")
            else:
                speak("Sorry, song not found in the music library.")
        else:
            speak("Please tell me the song name.")

    elif intent == "search_google":
        search_query = c.replace("search google", "").strip()

        if search_query:
            url = f"https://www.google.com/search?q={search_query}"
            webbrowser.open(url)
            speak(f"Searching Google for {search_query}")
        else:
            speak("Please tell me what to search.")

    elif intent == "search_wikipedia":
        topic = c.replace("search wikipedia", "").strip()

        if topic:
            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
                print(result)

            except Exception:
                speak("Sorry, I could not find that topic on Wikipedia.")
        else:
            speak("Please tell me the topic to search.")

    elif intent == "exit":
        speak("Goodbye. Have a great day.")
        exit()

    else:
        speak("Sorry, I did not understand that command.")


if __name__ == "__main__":
    speak("Initializing Jarvis")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = recognizer.listen(
                    source,
                    timeout=10,
                    phrase_time_limit=6
                )

            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes, I am listening")

                with sr.Microphone() as source:
                    print("Listening for command...")

                    audio = recognizer.listen(
                        source,
                        timeout=10,
                        phrase_time_limit=8
                    )

                    command = recognizer.recognize_google(audio)
                    print("Command:", command)

                    processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio")

        except sr.RequestError:
            print("Speech recognition service error")

        except Exception as e:
            print("Error:", e)