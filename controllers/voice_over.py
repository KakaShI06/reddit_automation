import pyttsx3
import os

voicePostDirectory = 'VoiceOvers'
voiceCmntDirectory = 'VoiceOvers'

def removeDir(path):
    os.rmdir(path=path)

def createVoiceOver(id, text, post_id):
    engine = pyttsx3.init()
    filePath = f"{voiceCmntDirectory}/post-{post_id}/comment-{id}.mp3"
    engine.save_to_file(text, filePath)
    engine.runAndWait()
    return filePath


def createVoiceOverPost(id, text):
    engine = pyttsx3.init()
    filePath = f"{voicePostDirectory}/post-{id}"
    os.mkdir(filePath)
    main_file_path = filePath + '/main.mp3'
    engine.save_to_file(text, main_file_path)
    engine.runAndWait()

    return filePath