import speech_recognition as sr
import urllib.request
import subprocess
from selenium.webdriver.common.by import By
import os


def download_audio(driver):
    downloadable = driver.find_element(By.XPATH, '//*[@id="rc-audio"]/div[7]/a')
    source = downloadable.get_attribute('href')
    urllib.request.urlretrieve(source, "captcha.mp3")

def mp32wav(mp3_path):
    subprocess.call(['ffmpeg', '-i', mp3_path, 'captcha.wav'], shell=False)
    os.remove("captcha.mp3")

def transcribe_audio_to_text(wav_path):
    recogizer=sr.Recognizer()
    with sr.AudioFile(wav_path)as source:
        audio=recogizer.record(source) 
    os.remove(wav_path)
    try:
        return recogizer.recognize_google(audio)
    except:
        print("audio to text error")