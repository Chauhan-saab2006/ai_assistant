import speech_recognition as sr
import webbrowser
import pyttsx3
import pyautogui
import time
import pyperclip
import datetime
import subprocess

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

# Speak function
def speak(text):
    """Speak the given text."""
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    # Listen for a command from the user using the microphone and return the recognized text.
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise to improve recognition accuracy
        print("Listening...")
        audio = recognizer.listen(source)  # Capture audio input from the microphone
        try:
            query = recognizer.recognize_google(audio, language="en-in")  # Recognize speech using Google API
            print(f"user said: {query}")
            return query.lower()  # Return the recognized text in lowercase
        except sr.UnknownValueError:
            # Handle case where speech was not understood
            print("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError as e:
            # Handle API request errors
            print(f"Could not request results from Google Speech Recognition service; {e}")
            return None
        except Exception as e:
            # Handle any other exceptions
            print("Some error occurred. Please try again.")
            return None
# it will open the sites based on the query

def open_sites(query):
    """Open specific websites based on the query."""
    sites = [
        ["youtube", "https://www.youtube.com"],
        ["wikipedia", "https://www.wikipedia.com"],
        ["google", "https://www.google.com"],
        ["instagram", "https://www.instagram.com"],
        ["whatsapp", "https://www.whatsapp.com"],
        ["github", "https://www.github.com"]
    ]
    for site in sites:
        if f"open {site[0]}" in query:
            speak(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
            return True
    return False

#  it will tell the time based on the query
def tell_time():
    """Tell the current time."""
    hour = datetime.datetime.now().strftime("%I")
    minute = datetime.datetime.now().strftime("%M")
    am_pm = datetime.datetime.now().strftime("%p")
    print(f"Sir, the time is {hour} {minute} {am_pm}") 
    speak(f"Sir, the time is {hour} {minute} {am_pm}") 

def exit_browser():
    """Close the current browser tab/window."""
    try:
        # Use keyboard shortcut to close tab (Ctrl+W)
        pyautogui.hotkey('ctrl', 'w')
        time.sleep(1)
        speak("Closed the browser tab")
    except Exception as e:
        print(f"Error closing browser: {e}")
        speak("Could not close the browser")
    
def play_music():
    """Play music on YouTube."""
    speak("Please tell me the name of the song.")
    song_name = takeCommand()
    if song_name:
        speak(f"Playing {song_name} on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
        time.sleep(5)
        pyautogui.click(x=282, y=533)  # Adjust coordinates for your screen resolution

def send_message():
    """Send a message on WhatsApp."""
    speak("Please tell me the message.")
    message = takeCommand()
    if message:
        speak("Please tell me the name of the contact.")
        contact = takeCommand()
        if contact:
            speak(f"Sending message to {contact}.")
            webbrowser.open("https://web.whatsapp.com/")
            time.sleep(10)  # Wait for WhatsApp Web to load
            pyperclip.copy(message)
            pyautogui.click(x=239, y=313)  # Adjust coordinates for the search bar
            time.sleep(3)
            pyautogui.write(contact)
            time.sleep(5)
            pyautogui.press("enter")
            time.sleep(2)
            pyautogui.click(x=1086, y=965)  # Adjust coordinates for the message box
            pyautogui.hotkey("ctrl", "v")
            time.sleep(2)
            pyautogui.press("enter")
            speak("Message sent successfully.")

def open_chrome(chrome):
    """
    Open an application using its executable path.

    Args:
        app_path (str): The full path to the application's executable file.
    """
    try:
        subprocess.Popen(chrome, shell=True)  # Open the application
        speak("Opening Chrome")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")
        
def open_cursor(cursor):
    try:
        subprocess.Popen(cursor, shell=True)  # Open the application
        speak("Opening cursor")
    except Exception as e:
        print(f"Failed to open the application: {e}")
        speak("Sorry, I couldn't open the application.")
   

# Main function
if __name__ == '__main__':
    print('ask me anything')
    speak("yes sir")
    while True:
        query = takeCommand()
        if query is None:
            continue  

        query = query.lower()  # Normalize input to lowercase

        # Check if "jarvis" is mentioned
        if "jarvis" not in query:
            continue  # Ignore everything else if jarvis is not mentioned

        # Remove the word "jarvis" to process commands easily
        query = query.replace("jarvis", "").strip()

        # Handle commands
        if open_sites(query):
            continue
        
        elif "time" in query:
            tell_time()
            
        elif "music" in query:
            play_music()
            
        elif "message" in query:
            send_message()
            
        elif "close" in query:
            speak("Exiting the site")
            exit()
       
        elif "shutdown" in query:  # Changed to handle "jarvis shutdown"
            speak("Goodbye, sir. Have a great day!")
            break
       
        elif "open chrome" in query:
            chrome_path = r"C:\Users\Public\Desktop\Google Chrome.lnk"  # Correct path to Chrome
            open_chrome(chrome_path)
       
        elif "open cursor" in query:
            cursor_path = r"C:\Users\lenovo\Desktop\Cursor.lnk"
            open_cursor(cursor_path)
       
        else:
            try:
                response = chat.send_message(query)
                print(f"{response.text}")
                speak(f"{response.text}")
            except Exception as e:
                print("Error:", e)
                    