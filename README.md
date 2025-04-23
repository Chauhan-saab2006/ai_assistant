# AI Assistant

This project is an AI assistant that utilizes speech recognition, web browsing, and text-to-speech functionalities. The assistant listens for the wake word "jarvis" and processes user commands to perform various tasks.

## Project Structure

```
ai-assistant
├── src
│   ├── main.py               # Entry point of the application
│   ├── modules
│   │   ├── speech_recognition.py  # Functions for speech recognition
│   │   ├── web_browsing.py        # Functions for web browsing tasks
│   │   └── text_to_speech.py      # Functions for text-to-speech functionality
├── requirements.txt          # List of dependencies
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies using the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage Guidelines

1. Run the application by executing the `main.py` file:

   ```
   python src/main.py
   ```

2. Once the application is running, say the wake word "jarvis" to activate the assistant.
3. Follow the prompts to give commands such as opening websites or sending messages.

## Dependencies

- speech_recognition
- pyttsx3
- pyautogui
- pyperclip
- datetime

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your contributions are welcome!