import speech_recognition as sr
import pywhatkit
import datetime
import pygame
import time

import say

pygame.init()
pygame.mixer.init()


def take_command():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print('monitoring your voice...')
        audio = listener.listen(source)

        try:
            command = listener.recognize_google(audio, language='en')
            print(f"user said:{command}\n")

        except Exception as e:
            return "None"
        return command


def run_glados():
    command = take_command().lower()
    if "hey glados" in command or "a glados" in command or "hey gladys" in command or "a gladys" in command or \
            "hey glad those" in command or "a glad those" in command:

        '''
        if "hey" in command:
            index = command.find("hey")
            command = command[index:]
            if "glados" in command:
                command = command.replace("hey glados ", "")
            elif "gladys" in command:
                command = command.replace("hey gladys ", "")
            elif "glad those" in command:
                command = command.replace("hey glad those ", "")
        elif "a" in command:
            index = command.find("a")
            command = command[index:]
            if "glados" in command:
                command = command.replace("a glados ", "")
            elif "gladys" in command:
                command = command.replace("a gladys ", "")
            elif "glad those" in command:
                command = command.replace("a glad those ", "")
        '''

        if "play" in command:
            print("playing")
            sound = pygame.mixer.Sound("GLaDOS VoiceWAV/playing_video.wav")  # GLaDOS voice "playing video"
            sound.play()
            time.sleep(1)
            video = command.replace("play ", "")
            if video == "play":
                pass
            else:
                print(video)
                pywhatkit.playonyt(video)
        elif "time" in command:
            sound = pygame.mixer.Sound("GLaDOS VoiceWAV/current_time_is.wav")  # GLaDOS voice "current time is"
            sound.play()
            time.sleep(1.55)

            time_hour = datetime.datetime.now().strftime("%I")
            say.number(time_hour)

            time_minute = datetime.datetime.now().strftime("%M")
            say.minute(time_minute)

            time_ampm = datetime.datetime.now().strftime("%p")
            say.ampm(time_ampm)

            print(time_hour + ":" + time_minute + time_ampm)
        elif "date" in command:
            sound = pygame.mixer.Sound("GLaDOS VoiceWAV/today_is.wav")  # GLaDOS voice "today is"
            sound.play()
            time.sleep(1)

            date_day = datetime.datetime.now().strftime("%d")
            say.number(date_day)

            # glados voice of
            sound = pygame.mixer.Sound("GLaDOS VoiceWAV/of.wav")  # GLaDOS voice "of"
            sound.play()
            time.sleep(0.5)
            date_month = datetime.datetime.now().strftime("%B")
            say.month(date_month)

            date_year = datetime.datetime.now().strftime("%Y")
            # glados voice 20
            sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/20.wav")  # GLaDOS voice "20"
            sound.play()
            time.sleep(0.5)
            date_year = date_year.replace("20", "")
            say.number(date_year)

            date_weekday = datetime.datetime.now().strftime("%A")
            say.weekday(date_weekday)

            print(date_month + " " + date_day + " " + "20" + date_year + " " + date_weekday)
        else:
            # GLaDOS voice "I don't get what are you talking coz I am a potato!!"
            sound = pygame.mixer.Sound("GLaDOS VoiceWAV/I don't get what are you talking cause I am a potato!.wav")
            sound.play()
            time.sleep(1.2)
            print("I don't get what are you talking cause I am a potato!!")
    else:
        run_glados()


while True:
    run_glados()
