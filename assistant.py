from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests
import pyttsx3
import mysql.connector
from weather import Weather

db = mysql.connector.connect(host="localhost", user="root", passwd="1234", database="assistant")
myCursor = db.cursor()
myCursor.execute('select acc_number from owner')
myResult = myCursor.fetchall()
#for i in myResult:
#    print(i)

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def instruct():
    "listens for instruction"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        instruction = r.recognize_google(audio).lower()
        print('You said: ' + instruction + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        talkToMe('Your last instruction couldn\'t be heard')
        instruction = myCommand();

    return instruction    

talkToMe('Hello, how may i help you?')

def account():
    talkToMe('We need to verify your identity for this. Please cooperate.')
    talkToMe('May I know your account number please?')
    acc_number = myCommand()
    talkToMe('you said your account number is '+acc_number+'. Is it right?')
    confirmation = myCommand()
    if confirmation!='it is':
        talkToMe('Please speak account number only. Let\'s try again!')
        account()
    else:
        talkToMe('please wait!')
        print(acc_number)
        if acc_number=='016 2480 2017':
            talkToMe('May I know your full name registered with bank?')
            full_name = myCommand()
            if full_name != 'rishikesh':
                talkToMe('this does not match with our database. Please try again later or contact customer support.')
            else:
                talkToMe('May I know your date of birth please. Keep in mind that you need to speak your date of birth in numbers. For example, if your date of birth is 15th August, 1990 You will say your date of birth as 1 5 0 8 1 9 9 0')
                dob = myCommand()
                if dob != '2008 1999':
                    talkToMe('Verification Unsuccessful. Let\'s start over.')
                    account()
                else:
                    talkToMe('Verification successful. Thanks for your cooperation.')
                    talkToMe('What do you need help with? Registering a complaint, Tracking complaint or an Agent?')
                    internal_commands(instruct())
        else:
            talkToMe('user does not exist.')
            account()
    return

def register():
    talkToMe('Okay! Go ahead and feel free to register a complaint. Please keep in mind that your complaint should be detailed containing all the necessary information. Once done, please say "That\'s it". Your grievance would be redressed within 7 business days and our customer support team may call you if required!')
    talkToMe('Listening')
    #We will listen and save the code here
    talkToMe('We have registered your complaint. We will try solve it within 7 business days.')
    token='8076321287'
    talkToMe('Your token has been generated. Your token number is: '+token+'. Keep this token safe for future reference. Have a great day. Goodbye')
    exit()

def trackin():
    talkToMe('tracking. please hold on.')

def internal_commands(instruction):
    if 'register a complaint' in instruction:
        register()
    elif 'track a complaint' in instruction:
        trackin()
    elif 'an agent' in instruction:
        talkToMe('Transferring your call. Please hold.')
    else:
        talkToMe('Currently we support only Registering a complaint, tracking a complaint and transferring call.')
        talkToMe('Do you want help with any of this?')
        option = myCommand()
        if option=='yes':
            talkToMe('you want help with?')
            internal_commands(instruct())
        else:
            internal_commands(instruct())

def assistant(command):
    "if statements for executing commands"

    if 'account' in command:
        account()

    # elif 'register a complaint' in command:
    #     register()

    # elif 'track a complaint' in command:
    #     trackin()

    elif 'agent' in command:
        talkToMe('Transferring your call. Please hold.')

    elif 'nothing' in command:
        talkToMe('Okay. Will talk to you later than. Have a great day!')
        exit()

    elif 'what\'s up' in command:
        talkToMe('Just doing my thing. How may I help you?')

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')

    elif 'haha' in command:
        talkToMe('I\'m glad you liked it.')
        
    elif 'shutdown' in command:
        talkToMe('Shutting down!')
        exit()

    else:
        talkToMe('I don\'t know what you mean!')
# def internal_commands(command):
#     if :
#         pass

#loop to continue executing multiple commands
while True:
    assistant(myCommand())