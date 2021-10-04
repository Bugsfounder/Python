# HEALTHY PROGRAMMER
# 9AM - 5PM
# WATER - water.mp3 (3.5 LITERS) - DRANK - LOG IN A FILE
# EYES - eyes.mp3 - EVERY 30 MINUTES  - EyDone - LOG IN A FILE
# PHYSICAL ACTIVITY - physical.mp3 - EVERY 45 MINUTES - ExDone - LOG IN A FILE

# RULES
# USE PYGAME MODULE TO PLAY AUDIO

from pygame import mixer
import schedule
import time


# FUNCTIONS
def playAudio(songName, workName, message):
    """
    This function is just playing audio taking audio name as parameter and some more parameters
    :param songName: string
    :param workName: string
    :param message: string
    :return: nothing
    """
    # Starting the mixer
    mixer.init()
    # Loading the song
    mixer.music.load(f"{songName}")
    # Setting the volume
    mixer.music.set_volume(0.7)
    # Start playing the song
    mixer.music.play(-1)
    # infinite loop
    while True:
        now = datetime.now()
        print(f"{message}")
        query = input(f"If You Done Than Press '{workName}' to Stop: ")
        f = open(f"{workName.lower()}.txt", "+a")
        f.write(f"[{now}] {query}\n")
        if query == 'p':
            # Pausing the music
            mixer.music.pause()
        elif query == 'r':
            # Resuming the music
            mixer.music.unpause()
        elif query == f'{workName}':
            # Stop the mixer
            mixer.music.stop()
        break


import schedule
import time
from datetime import datetime

# If the current time is 11 P.M of 2013-11-05 and I want to get the timestamp for 9 A.M 2013-11-06

dt = datetime.today().strftime("%H:%M %p")
h = datetime.today().strftime("%H")
p = datetime.today().strftime("%p")
# print(dt)
# print(type(h))
# print(type(p))

if (h >= "9" and p == "AM") or (h <= "12" and p == "AM"):
    # schedule.every(1).minutes.do(lambda: playAudio("eye.mp3", "EyDone", "Eye Relaxing Time"))
    schedule.every(30).minutes.do(lambda: playAudio("eye.mp3", "EyDone", "Eye Relaxing Time"))
    schedule.every(45).minutes.do(lambda: playAudio("exercise.mp3", "ExDone", "Time to Do Some Exercise"))
    schedule.every(2).hours.do(lambda: playAudio("water.mp3", "Drank", "Time to Drink Some Water"))
    while 1:
        schedule.run_pending()
        time.sleep(1)

elif (h >= "1" and p == "PM") or (h <= "5" and p == "PM"):
    schedule.every(30).minutes.do(lambda: playAudio("eye.mp3", "EyDone", "Eye Relaxing Time"))
    schedule.every(45).minutes.do(lambda: playAudio("exercise.mp3", "ExDone", "Time to Do Some Exercise"))
    schedule.every(2).hours.do(lambda: playAudio("water.mp3", "Drank", "Time to Drink Some Water"))
    while 1:
        schedule.run_pending()
        time.sleep(1)
else:
    print('Welcome to Healthy Programmer Programme')
