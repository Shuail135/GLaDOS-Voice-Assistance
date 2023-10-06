import pygame
import time


def minute(minute):
    if minute == "01":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O1.wav")  # GLaDOS voice "o1"
        sound.play()
        time.sleep(0.7)
    elif minute == "02":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O2.wav")  # GLaDOS voice "o2"
        sound.play()
        time.sleep(0.75)
    elif minute == "03":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O3.wav")  # GLaDOS voice "o3"
        sound.play()
        time.sleep(0.7)
    elif minute == "04":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O4.wav")  # GLaDOS voice "o4"
        sound.play()
        time.sleep(0.8)
    elif minute == "05":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O5.wav")  # GLaDOS voice "o5"
        sound.play()
        time.sleep(0.8)
    elif minute == "06":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O6.wav")  # GLaDOS voice "o6"
        sound.play()
        time.sleep(0.9)
    elif minute == "07":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O7.wav")  # GLaDOS voice "o7"
        sound.play()
        time.sleep(1.2)
    elif minute == "08":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O8.wav")  # GLaDOS voice "o8"
        sound.play()
        time.sleep(0.7)
    elif minute == "09":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/O9.wav")  # GLaDOS voice "o9"
        sound.play()
        time.sleep(1)
    else:
        number(minute)


def number(number):
    # glados voice 00 to 59
    if number == "01":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/1.wav")  # GLaDOS voice "1"
        sound.play()
        time.sleep(0.7)
    elif number == "02":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/2.wav")  # GLaDOS voice "2"
        sound.play()
        time.sleep(0.75)
    elif number == "03":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/3.wav")  # GLaDOS voice "3"
        sound.play()
        time.sleep(0.7)
    elif number == "04":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/4.wav")  # GLaDOS voice "4"
        sound.play()
        time.sleep(0.8)
    elif number == "05":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/5.wav")  # GLaDOS voice "5"
        sound.play()
        time.sleep(0.75)
    elif number == "06":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/6.wav")  # GLaDOS voice "6"
        sound.play()
        time.sleep(0.9)
    elif number == "07":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/7.wav")  # GLaDOS voice "7"
        sound.play()
        time.sleep(1.2)
    elif number == "08":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/8.wav")  # GLaDOS voice "8"
        sound.play()
        time.sleep(0.7)
    elif number == "09":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/9.wav")  # GLaDOS voice "9"
        sound.play()
        time.sleep(1)
    elif number == "10":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/10.wav")  # GLaDOS voice "10"
        sound.play()
        time.sleep(0.9)
    elif number == "11":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/11.wav")  # GLaDOS voice "11"
        sound.play()
        time.sleep(1)
    elif number == "12":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/12.wav")  # GLaDOS voice "12"
        sound.play()
        time.sleep(0.9)
    elif number == "13":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/13.wav")  # GLaDOS voice "13"
        sound.play()
        time.sleep(1)
    elif number == "14":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/14.wav")  # GLaDOS voice "14"
        sound.play()
        time.sleep(1.3)
    elif number == "15":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/15.wav")  # GLaDOS voice "15"
        sound.play()
        time.sleep(1.15)
    elif number == "16":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/16.wav")  # GLaDOS voice "16"
        sound.play()
        time.sleep(1.3)
    elif number == "17":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/17.wav")  # GLaDOS voice "17"
        sound.play()
        time.sleep(1.3)
    elif number == "18":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/18.wav")  # GLaDOS voice "18"
        sound.play()
        time.sleep(1.1)
    elif number == "19":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/19.wav")  # GLaDOS voice "19"
        sound.play()
        time.sleep(1.2)
    elif number == "20":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/20.wav")  # GLaDOS voice "20"
        sound.play()
        time.sleep(0.8)
    elif number == "21":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/21.wav")  # GLaDOS voice "21"
        sound.play()
        time.sleep(1.1)
    elif number == "22":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/22.wav")  # GLaDOS voice "22"
        sound.play()
        time.sleep(1.1)
    elif number == "23":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/23.wav")  # GLaDOS voice "23"
        sound.play()
        time.sleep(1.2)
    elif number == "24":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/24.wav")  # GLaDOS voice "24"
        sound.play()
        time.sleep(1.2)
    elif number == "25":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/25.wav")  # GLaDOS voice "25"
        sound.play()
        time.sleep(1.2)
    elif number == "26":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/26.wav")  # GLaDOS voice "26"
        sound.play()
        time.sleep(1.23)
    elif number == "27":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/27.wav")  # GLaDOS voice "27"
        sound.play()
        time.sleep(1.15)
    elif number == "28":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/28.wav")  # GLaDOS voice "28"
        sound.play()
        time.sleep(1)
    elif number == "29":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/29.wav")  # GLaDOS voice "29"
        sound.play()
        time.sleep(1.1)
    elif number == "30":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/30.wav")  # GLaDOS voice "30"
        sound.play()
        time.sleep(0.8)
    elif number == "31":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/31.wav")  # GLaDOS voice "31"
        sound.play()
        time.sleep(1.2)
    elif number == "32":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/32.wav")  # GLaDOS voice "32"
        sound.play()
        time.sleep(1.3)
    elif number == "33":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/33.wav")  # GLaDOS voice "33"
        sound.play()
        time.sleep(1.3)
    elif number == "34":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/34.wav")  # GLaDOS voice "34"
        sound.play()
        time.sleep(1.2)
    elif number == "35":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/35.wav")  # GLaDOS voice "35"
        sound.play()
        time.sleep(1.1)
    elif number == "36":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/36.wav")  # GLaDOS voice "36"
        sound.play()
        time.sleep(1.2)
    elif number == "37":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/37.wav")  # GLaDOS voice "37"
        sound.play()
        time.sleep(1.2)
    elif number == "38":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/38.wav")  # GLaDOS voice "38"
        sound.play()
        time.sleep(1)
    elif number == "39":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/39.wav")  # GLaDOS voice "39"
        sound.play()
        time.sleep(1.2)
    elif number == "40":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/40.wav")  # GLaDOS voice "40"
        sound.play()
        time.sleep(0.9)
    elif number == "41":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/41.wav")  # GLaDOS voice "41"
        sound.play()
        time.sleep(1.2)
    elif number == "42":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/42.wav")  # GLaDOS voice "42"
        sound.play()
        time.sleep(1.3)
    elif number == "43":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/43.wav")  # GLaDOS voice "43"
        sound.play()
        time.sleep(1.3)
    elif number == "44":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/44.wav")  # GLaDOS voice "44"
        sound.play()
        time.sleep(1.3)
    elif number == "45":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/45.wav")  # GLaDOS voice "45"
        sound.play()
        time.sleep(1.25)
    elif number == "46":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/46.wav")  # GLaDOS voice "46"
        sound.play()
        time.sleep(1.25)
    elif number == "47":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/47.wav")  # GLaDOS voice "47"
        sound.play()
        time.sleep(1.2)
    elif number == "48":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/48.wav")  # GLaDOS voice "48"
        sound.play()
        time.sleep(1.1)
    elif number == "49":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/49.wav")  # GLaDOS voice "49"
        sound.play()
        time.sleep(1.25)
    elif number == "50":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/50.wav")  # GLaDOS voice "50"
        sound.play()
        time.sleep(1)
    elif number == "51":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/51.wav")  # GLaDOS voice "51"
        sound.play()
        time.sleep(1.2)
    elif number == "52":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/52.wav")  # GLaDOS voice "52"
        sound.play()
        time.sleep(1.15)
    elif number == "53":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/53.wav")  # GLaDOS voice "53"
        sound.play()
        time.sleep(1.2)
    elif number == "54":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/54.wav")  # GLaDOS voice "54"
        sound.play()
        time.sleep(1.3)
    elif number == "55":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/55.wav")  # GLaDOS voice "55"
        sound.play()
        time.sleep(1.3)
    elif number == "56":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/56.wav")  # GLaDOS voice "56"
        sound.play()
        time.sleep(1.4)
    elif number == "57":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/57.wav")  # GLaDOS voice "57"
        sound.play()
        time.sleep(1.25)
    elif number == "58":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/58.wav")  # GLaDOS voice "58"
        sound.play()
        time.sleep(1.2)
    elif number == "59":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Number/59.wav")  # GLaDOS voice "59"
        sound.play()
        time.sleep(1.2)


def ampm(ampm):
    # glados voice am/pm
    if ampm == "AM":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/am.wav")  # GLaDOS voice "am"
        sound.play()
        time.sleep(1)
    elif ampm == "PM":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/pm.wav")  # GLaDOS voice "pm"
        sound.play()
        time.sleep(1)


def month(month):
    # glados voice January to December
    if month == "January":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/January.wav")  # GLaDOS voice "January"
        sound.play()
        time.sleep(1)
    elif month == "February":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/February.wav")  # GLaDOS voice "February"
        sound.play()
        time.sleep(1.2)
    elif month == "March":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/March.wav")  # GLaDOS voice "March"
        sound.play()
        time.sleep(0.8)
    elif month == "April":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/April.wav")  # GLaDOS voice "April"
        sound.play()
        time.sleep(0.7)
    elif month == "June":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/June.wav")  # GLaDOS voice "June"
        sound.play()
        time.sleep(0.7)
    elif month == "July":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/July.wav")  # GLaDOS voice "July"
        sound.play()
        time.sleep(0.8)
    elif month == "August":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/August.wav")  # GLaDOS voice "August"
        sound.play()
        time.sleep(0.8)
    elif month == "September":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/September.wav")  # GLaDOS voice "September"
        sound.play()
        time.sleep(1)
    elif month == "October":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/October.wav")  # GLaDOS voice "October"
        sound.play()
        time.sleep(0.95)
    elif month == "November":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/November.wav")  # GLaDOS voice "November"
        sound.play()
        time.sleep(0.95)
    elif month == "December":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Month/December.wav")  # GLaDOS voice "December"
        sound.play()
        time.sleep(0.9)


def weekday(weekday):
    # glados voice Monday to Sunday
    if weekday == "Monday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Monday.wav")  # GLaDOS voice "Monday"
        sound.play()
        time.sleep(1.2)
    elif weekday == "Tuesday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Tuesday.wav")  # GLaDOS voice "Tuesday"
        sound.play()
        time.sleep(1)
    elif weekday == "Wednesday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Wednesday.wav")  # GLaDOS voice "Wednesday"
        sound.play()
        time.sleep(0.95)
    elif weekday == "Thursday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Thursday.wav")  # GLaDOS voice "Thursday"
        sound.play()
        time.sleep(0.9)
    elif weekday == "Friday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Friday.wav")  # GLaDOS voice "Friday"
        sound.play()
        time.sleep(0.9)
    elif weekday == "Saturday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Saturday.wav")  # GLaDOS voice "Saturday"
        sound.play()
        time.sleep(1)
    elif weekday == "Sunday":
        sound = pygame.mixer.Sound("GLaDOS VoiceWAV/Weekday/Sunday.wav")  # GLaDOS voice "Sunday"
        sound.play()
        time.sleep(0.9)