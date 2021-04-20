import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
listener = sr.Recognizer()
name_of_assistant = "Safi"

eng_speaker = pyttsx3.init()
#Set female voice
eng_speaker.setProperty('voice', eng_speaker.getProperty('voices')[1].id)

def speak(text):
    eng_speaker.say(text)
    eng_speaker.runAndWait()


def take_input_command():
    voice_command=""
    try:
        with sr.Microphone() as src:
            speak("Hey there, I am"+ name_of_assistant+", How can I help you?")
            voice = listener.listen(src)
            

            voice_command = listener.recognize_google(voice)
            voice_command = voice_command.lower()

            if name_of_assistant in voice_command:
                voice_command = voice_command.replace(name_of_assistant, "")
            
                # print("Your command: "+voice_command)

    except:
        pass
    

    return voice_command 

def main():
    command = take_input_command()
    print(command)


    #Playing a video on youtube
    if 'play' in command:
        command = command.replace("play", "")

        speak("playing"+command+" youtube")
        pywhatkit.playonyt(command)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak("The current time is "+time)
    
    #Searching for someone on wikipedia

    elif 'who is' in command:
        command = command.replace('who is', '')
        response = wikipedia.summary(command, 5)
        print(response)
        speak(response)
        
    #plays notes that users asks ex "piano c2 a2"
    elif 'piano' in command:
        command = command.replace('piano', '')
        notes = command.split(" ", 1000)
        piano.play_song(notes)

    

main()


#https://www.lfd.uci.edu/~gohlke/pythonlibs
