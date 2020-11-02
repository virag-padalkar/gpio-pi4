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
        print("Enter voice command!\n")
        audio = r.listen(source,phrase_time_limit=5)
        print ("Audio captured . . please wait")
    response = r.recognize_google(audio)
    return response

# function to operate gpio via output of audio capture function above
def operate_gpio():
    response = capture_audio()
    if "switch on" in response:
        print ("Switching on LED for 5 seconds\n")
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        GPIO.output(18, GPIO.HIGH)
        time.sleep(5)
        GPIO.output(18, GPIO.LOW)
        GPIO.cleanup()
        print ("Switching off LED")
    else:
        print ("Incorrect command, terminating program")

# main
def main():
	operate_gpio()

if __name__ == "__main__":
    main()