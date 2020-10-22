
def takeCommand():
    #it takes microphone input from the user and converts into string
    r=sr.Recognizer()
    with sr.Microphone() as source: