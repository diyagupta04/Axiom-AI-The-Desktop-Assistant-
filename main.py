import pyautogui
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pywhatkit as wk
import os
import subprocess
import datetime
import time
import cv2
import random
import sys
import operator
import requests

engine = pyttsx3.init()
'''voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 200)'''

def speak(audio):
    """Speak the given text."""
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    """Greet the user based on the current time."""
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Noon!")
    else:
        speak("Good Evening!")

    speak("Ready to comply. What can I do for you?")

def takeCommand():
    """Listen and recognize the user's speech."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def open_textedit_and_write():
    """Open TextEdit and write text using voice recognition."""
    try:
        # Open TextEdit
        print("Opening TextEdit...")
        os.system("open -a TextEdit")
        time.sleep(3)  # Wait for TextEdit to open

        # Use AppleScript to bring TextEdit to the foreground
        osascript_focus_textedit = """
        tell application "TextEdit"
            activate
        end tell
        """
        subprocess.call(["osascript", "-e", osascript_focus_textedit])
        time.sleep(2)  # Allow time for focus

        # Create a new document if needed
        print("Ensuring focus on TextEdit...")
        pyautogui.hotkey('command', 'n')  # New document
        time.sleep(2)

        # Ask for user input via voice recognition
        speak("Please say the text you want to write in TextEdit.")
        recognized_text = takeCommand()

        if recognized_text and recognized_text.lower() != "none":
            # Ensure focus on the text area by clicking it
            print("Writing text in TextEdit...")
            pyautogui.click(200, 200)  # Adjust coordinates if needed
            time.sleep(1)
            pyautogui.write(recognized_text, interval=0.1)  # Type the recognized text
            speak("Your text has been written in TextEdit.")
        else:
            speak("I couldn't recognize any text. Please try again.")

    except Exception as e:
        print(f"Error: {e}")
        speak("I encountered an error while trying to write in TextEdit.")

def draw_line(start_x, start_y, end_x, end_y, duration=1):
    """
    Parameters:
    start_x, start_y : int : Starting coordinates of the line.
    end_x, end_y : int : Ending coordinates of the line.
    duration : float : Duration of the drag (default: 1 second).
    """
    try:
                # Move to the starting point
        print(f"Moving to starting position: ({start_x}, {start_y})")
        pyautogui.moveTo(start_x, start_y, duration=0.5)

                # Simulate mouse press and drag
        print(f"Drawing line to: ({end_x}, {end_y})")
        pyautogui.mouseDown()
        pyautogui.moveTo(end_x, end_y, duration=duration)
        pyautogui.mouseUp()

        print("Line drawing complete.")
    except Exception as e:
        print(f"Error while drawing the line: {e}")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'axiom' in query:
            print("Yes")
            speak("Yes")

        elif "type" in query:
            query=query.replace("type","")
            pyautogui.typewrite(f"{query}",0.1)

        elif 'who are you' in query:
            speak('I am Axiom, a desktop assistant. I have been made to make your interaction with your desktop a friendlier one.')

        elif 'who created you' in query:
            speak('The owner of this laptop has created me using a programming language called Python.')

        elif "what is the time" in query:
            now = datetime.datetime.now()
            hours = now.strftime("%H")
            minutes = now.strftime("%M")
            seconds = now.strftime("%S")
            speak(f"The time is {hours} hours, {minutes} minutes, and {seconds} seconds.")

        elif "what is my ip address" in query:
            speak("Checking your IP address. Please wait.")
            try:
                # Fetch the public IP address from the ipify API
                ipAdd = requests.get("https://api.ipify.org").text
                print(f"Your IP Address is: {ipAdd}")
                speak(f"Your IP address is {ipAdd}")
            except requests.exceptions.RequestException as e:
                # Handle network errors gracefully
                print(f"Error fetching IP address: {e}")
                speak("I couldn't fetch your IP address. Please check your internet connection and try again.")

        elif 'what is' in query:
            speak("Searching Wikipedia...")
            query = query.replace("what is", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia,")
                print(results)
                speak(results)
            except wikipedia.DisambiguationError as e:
                speak("The query returned multiple results. Please be more specific.")
                print(e.options)
            except wikipedia.PageError:
                speak("No results found on Wikipedia.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")

        elif 'who is' in query:
            speak("Searching Wikipedia...")
            query = query.replace("who is", "").strip()
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia,")
                print(results)
                speak(results)
            except wikipedia.DisambiguationError as e:
                speak("The query returned multiple results. Please be more specific.")
                print(e.options)
            except wikipedia.PageError:
                speak("No results found on Wikipedia.")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")

        elif 'just open google' in query:
            webbrowser.open('https://www.google.com')

        elif 'open google' in query:
            speak("What should I search?")
            qry = takeCommand().lower()
            if qry != "None":
                webbrowser.open(f"https://www.google.com/search?q={qry}")
                try:
                    results = wikipedia.summary(qry, sentences=2)
                    speak("According to Wikipedia,")
                    print(results)
                    speak(results)
                except wikipedia.DisambiguationError as e:
                    speak("The query returned multiple results. Please be more specific.")
                    print(e.options)
                except wikipedia.PageError:
                    speak("No results found on Wikipedia.")
                except Exception as e:
                    speak("An error occurred.")
            else:
                speak("I couldn't understand your query.")

        elif 'just open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open youtube' in query:
            speak("What would you like to watch?")
            qrry = takeCommand().lower()
            if qrry != "None":
                wk.playonyt(qrry)
            else:
                speak("I couldn't understand your query.")

        elif "search on youtube" in query:
            query = query.replace("search on youtube", "").strip()
            if query:
                webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
            else:
                speak("I couldn't understand your query.")

        elif "close browser" in query:
            try:
                os.system("killall 'Google Chrome'")  # Close Google Chrome
                os.system("killall 'Microsoft Edge'")  # Close Microsoft Edge
                speak("Browser has been closed.")
            except Exception as e:
                speak("I couldn't close the browser. Please try again.")
                print(e)

        elif "close safari" in query:
            try:
                os.system("killall 'Safari'")  # Close Safari
                speak("Safari has been closed.")
            except Exception as e:
                speak("I couldn't close Safari. Please try again.")
                print(e)

        elif "open free form" in query:
            app_path = "/System/Applications/Freeform.app"
            if os.path.exists(app_path):
                subprocess.call(["open", app_path])
            else:
                speak("Freeform application not found.")

        elif "close free form" in query:
            try:
                os.system("killall 'Freeform'")
                speak("Freeform has been closed.")
            except Exception as e:
                speak("An error occurred while trying to close Freeform.")
                print(e)

        elif "play music" in query:
            try:
                # Use AppleScript to open and play the Music app
                apple_script = """
                tell application "Music"
                    activate
                    play
                end tell
                """
                subprocess.call(["osascript", "-e", apple_script])  # Execute the AppleScript
                speak("Playing music from your library.")
            except Exception as e:
                speak("I couldn't open and play music.")
                print(e)

        elif "stop music" in query or "close music" in query:
            try:
                # Pause music first
                pause_script = """
                tell application "Music"
                    pause
                end tell
                """
                subprocess.call(["osascript", "-e", pause_script])

                # Close the Music app
                os.system("killall 'Music'")
                speak("Music has been stopped and the app is closed.")
            except Exception as e:
                speak("I couldn't close the Music app.")
                print(f"Error: {e}")


        elif "stop music" in query:
                os.system("killall 'Music'")
                speak("Music has been stopped and the app is closed.")

        # Shutdown system
        elif "shutdown the system" in query:
            shutdown_script = """
            tell application "System Events"
                shut down
            end tell
            """
            subprocess.call(["osascript", "-e", shutdown_script])

        # Restart system
        elif "restart the system" in query:
            restart_script = """
            tell application "System Events"
                restart
            end tell
            """
            subprocess.call(["osascript", "-e", restart_script])

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('Webcam',img)
                k=cv2.waitKey(50)
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()

        elif "go to sleep" in query:
            speak("Alright then, I am switching off!")
            sys.exit()

        elif "take screenshot" in query:
            speak("Tell me a name for this file.")
            name = takeCommand().lower()

            if name == "none" or not name.strip():
                speak("I couldn't understand the name. Please try again.")
            else:
                try:
                # Ensure the name is valid by replacing invalid characters
                    valid_name = "".join(c if c.isalnum() else "_" for c in name)

                # Set the save path
                    save_path = os.path.join(os.path.expanduser("~"), f"{valid_name}.png")

                    speak("Taking screenshot in 3 seconds.")
                    time.sleep(3)

                # Capture and save the screenshot
                    img = pyautogui.screenshot()
                    img.save(save_path)

                    speak(f"Screenshot saved as {valid_name}.png in your home directory.")
                    print(f"Screenshot saved at: {save_path}")

                except Exception as e:
                    speak("An error occurred while taking the screenshot. Please try again.")
                    print(f"Error: {e}")

        elif "calculate" in query:
            try:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("What do you want to calculate?")
                    print("Listening for calculation...")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)

                my_string = r.recognize_google(audio).lower()
                print(f"Calculation input: {my_string}")

                # Replace words for operators with symbols
                my_string = my_string.replace("plus", "+")
                my_string = my_string.replace("minus", "-")
                my_string = my_string.replace("times", "*")
                my_string = my_string.replace("multiplied by", "*")
                my_string = my_string.replace("divided by", "/")
                my_string = my_string.replace("divide", "/")


                # Parse and evaluate the expression
                def get_operator_fn(op):
                    return {
                        '+': operator.add,
                        '-': operator.sub,
                        '*': operator.mul,
                        '/': operator.truediv,
                    }[op]


                def eval_binary_expr(op1, oper, op2):
                    op1, op2 = float(op1), float(op2)  # Support for decimals
                    return get_operator_fn(oper)(op1, op2)


                tokens = my_string.split()
                result = eval_binary_expr(tokens[0], tokens[1], tokens[2])
                speak(f"The result is {result}")
                print(f"Result: {result}")

            except Exception as e:
                speak("I couldn't process the calculation. Please try again.")
                print(f"Error: {e}")

        # Volume Up
        elif "volume up" in query:
            if query.count("volume") == 1:
                speak("Increasing volume.")
                try:
                    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) + 10)'")
                except Exception as e:
                    speak("I couldn't increase the volume. Please try again.")
                    print(f"Error: {e}")

        elif "volume down" in query or "volume low" in query:
            if query.count("volume") == 1:  # Execute only once per trigger
                speak("Decreasing volume.")
                try:
                    os.system("osascript -e 'set volume output volume (output volume of (get volume settings) - 10)'")
                except Exception as e:
                    speak("I couldn't decrease the volume. Please try again.")
                    print(f"Error: {e}")

        # Mute Command
        elif "mute" in query:
            speak("Muting the volume.")
            try:
                os.system("osascript -e 'set volume with output muted'")
                speak("The system is now muted.")
            except Exception as e:
                speak("I couldn't mute the volume. Please try again.")
                print(f"Error: {e}")

        # Unmute Command
        elif "Unmute" in query:
            speak("Unmuting the volume.")
            try:
                # Unmute and set volume to a default level if needed
                os.system("osascript -e 'set volume without output muted'")
                os.system("osascript -e 'set volume output volume 50'")  # Optional: Restore volume to 50%
                speak("The system is now unmuted.")
            except Exception as e:
                speak("I couldn't unmute the volume. Please try again.")
                print(f"Error: {e}")

        elif "open text edit and write" in query:
            open_textedit_and_write()

        elif "draw a line" in query:
            print("Switch to the Flow Free app within 5 seconds...")
            time.sleep(5)

            # Define start and end points with the provided coordinates
            start_coordinates = (1211, 55)  # Starting coordinates (x=1211, y=55)
            end_coordinates = (600, 400)  # Define your ending coordinates here

            # Call the function to draw the line
            draw_line(*start_coordinates, *end_coordinates)


        elif "stop assistant" in query:
            speak("Goodbye!")
            sys.exit()



























