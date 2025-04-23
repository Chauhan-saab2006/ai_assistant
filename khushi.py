import speech_recognition as sr
import webbrowser
import pyttsx3
import pyautogui
import time
import pyperclip
import datetime

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Set the voice to female
voices = engine.getProperty('voices')

print("Available voices:")
for voice in voices:
    print(f"Voice ID: {voice.id}, Name: {voice.name}")

for voice in voices:
    if "zira" in voice.name.lower():  # Replace "zira" with the desired female voice name
        engine.setProperty('voice', voice.id)
        print(f"Female voice set to: {voice.name}")
        break
    else:
         print("Female voice not found. Using default voice.")
def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    """Process the user's command."""
    if "open google" in c.lower():
        print("Opening Google")
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c.lower():
        print("Opening YouTube")
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open whatsapp" in c.lower():
        print("Opening WhatsApp")
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")

    elif "open github" in c.lower():
        print("Opening GitHub")
        speak("Opening GitHub")
        webbrowser.open("https://www.github.com")
    

    elif "music" in c.lower():        
        speak("please tell me the song name")
        with sr.Microphone() as source:
            print("listening.......")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
            song_name = recognizer.recognize_google(audio).lower()
            print(f"song_name:{song_name}")
            time.sleep(1)
           # Open YouTube and search for the song
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            time.sleep(5)  # Wait for the page to load    
        pyautogui.click(x=282, y=533)  
        speak("Enjoy your music!")
                 
    elif "message" in c.lower():
        # Get the message from the user
            speak("please tell me the message")
            with sr.Microphone() as source:
                print("listening.......")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                message = recognizer.recognize_google(audio).lower()
                print(f"message:{message}")
        # Get the contact name from the user
            speak("Please tell me the name of the contact.")
            with sr.Microphone() as source: 
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                contact = recognizer.recognize_google(audio).lower()
                print(f"contact:{contact}")
                speak(f"sending message to {contact}")            
        # open whatsapp web
                webbrowser.open("https://web.whatsapp.com/")
                time.sleep(8)   # wait for the page to load    
        # Copy the message to the clipboard
                pyperclip.copy(message)    
        # Search for the contact and send the message
                pyautogui.click (x=239, y=313)              
                time.sleep(3)  
        # it search the contact name in the search bar of whatsapp                       
                pyautogui.write(contact) 
                time.sleep(5)
        # it click on the first contact of the whatsapp        
                pyautogui.press("enter")  
                time.sleep(2)
        # it click on the message input box of whatsapp        
                pyautogui.click(x=1086, y=965)  
        # it paste the message from the clipboard        
                pyautogui.hotkey("ctrl", "v")  
                time.sleep(2)
        # it click on the send button of whatsapp        
                pyautogui.press("enter")                 
                speak("Message sent successfully.")
                        
    # it colose the page in which is open
    elif "exit" in c.lower():
          pyautogui.click (x=1881, y=21) 
          time.sleep(3)     
    
    elif "time" in c.lower():
        # Get the current time in 12-hour format with AM/PM
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        print(f"The time is {current_time}") 
        speak(f"The time is {current_time}") 
    
    elif "switch off" in c.lower():
        speak("Goodbye sir i am going to sleep")
        exit()

    else:
        speak("Sorry, I didn't understand ")

if __name__ == "__main__":
    speak("Initializing khushi...")
    while True:
        try:
            # Listen for the keyword "khushi"
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)  
                print("Listening for the keyword 'khushi'...")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                word = recognizer.recognize_google(audio).lower()

            if "khushi" in word:
                speak("Yes sir")
                # Listen for the actual command
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("khushi is active. Listening for your command...")
                    audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio).lower()

                # Process the command
                processcommand(command)

        except sr.WaitTimeoutError:
            print("Listening timed out. Restarting...")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")