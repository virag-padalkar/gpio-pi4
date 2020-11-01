#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 21:24:09 2020

@author: virag
"""
# import libraries
import RPi.GPIO as GPIO
import time
import speech_recognition as sr

# function to capture audio using default mic and parse audio to text
def capture_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Say something!")
        audio = r.listen(source,phrase_time_limit=5)
        print ("Audio captured")
    global response
    response = r.recognize_google(audio)
    return response

# function to operate gpio via output of audio capture function above
def operate_gpio():
    capture_audio()
    if "switch on" in response:
        print ("Switching on LED")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()
    else:
        print ("Incorrect command")

# run the program
operate_gpio()