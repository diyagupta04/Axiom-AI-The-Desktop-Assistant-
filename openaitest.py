import pyautogui
print(pyautogui.position())  # Move the mouse over the chat input box and run this to get the coordinates


import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import pyautogui
import time

def say(text):
    os.system(f"say {text}")

def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        #r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "SOME ERROR OCCURRED. SORRY FROM AXIOM"

if __name__=='__main__':
    print('PyCharm')
    say("Hello I am Axiom A.I.")
    while True:
        print("Listening...")
        query = takeCommand()
        sites=[["YouTube","https://www.youtube.com"],["wikipedia","https://www.wikipedia.com"],["google","https://www.google.com"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath="/Users/diyagupta/Downloads/galaxy-226963.mp3"
            os.system(f"open {musicPath}")

        if "the time" in query:
            strfTime=datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        #say(query)

        if "search chat gpt for" in query.lower():
            search_query = query.lower().replace("search chat gpt for", "").strip()
            say(f"Searching ChatGPT for {search_query}")
            webbrowser.open("https://chat.openai.com/")  # Open ChatGPT in a browser

            # Give the browser time to load
            time.sleep(7)

            # Ensure the browser is focused (use alt+tab for Windows or command+tab for Mac)
            pyautogui.hotkey('command', 'tab')  # Use 'alt' for Windows

            # Wait for the browser to come into focus
            time.sleep(2)

            # Click on the chat input box (adjust x, y to match your screen resolution)
            # Make sure you update these coordinates to the actual chat box position
            pyautogui.click(x=768, y=52)

            # Add a slight pause to ensure the input box is ready for typing
            time.sleep(1)

            # Type the query into the input box with a delay to simulate human typing
            pyautogui.typewrite(search_query, interval=0.1)

            # Press Enter to submit the query
            pyautogui.press("enter")

            # Add a brief pause to allow the action to complete
            time.sleep(2)
