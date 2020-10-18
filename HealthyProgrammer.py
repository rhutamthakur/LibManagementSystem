from datetime import datetime
import time
from pygame import mixer

def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input("Confirm action completion:")
        if a== stopper:
            mixer.music.stop()
            break

def healthLogs(comment):
    with open("HealthyProgrammer.txt","a") as p:
        p.write(f"{comment} Time:{datetime.now()}")

def waterReminder():
    time.sleep(5)
    musiconloop("Water.mp3","Drank Water")
    healthLogs("Drank Water")

def eyesReminder():
    time.sleep(10)
    musiconloop("Eyes.mp3","Blinked Eyes")
    healthLogs("Blinked Eyes")

def exerciseReminder():
    time.sleep(15)
    musiconloop("Exercise.mp3","Exercised")
    healthLogs("Exercised")



ml_of_water = 2000
while True:
    if ml_of_water>0:
        waterReminder()
        ml_drunk = int(input("How much water did you drink?:"))
        ml_of_water = ml_of_water - ml_drunk
    else:
        print("You have had your quota of water today!")
    eyesReminder()
    exerciseReminder()
    ans=input("Do you wish to end the program?(Y/N):")
    if ans==Y or ans==y:
        break
    else:
        continue
