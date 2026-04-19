import time
def speak(text, delay=3):
    print(text)
    time.sleep(delay)

speak("Hello there, my name is Bob",3)
speak("What are you doing today?",3)
speak("Very interesting",0)