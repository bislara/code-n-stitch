import speech_recognition as sr
filename = "sample.wav"

# Initializing speech recognizer
r = sr.Recognizer()

# Opening the file
with sr.AudioFile(filename) as source:
    # Loading audio data onto memory
    audio_data = r.record(source)
    print('Audio data successfully loaded onto memory.\nConverting speech to text...')
    # Recognizing speech and converting to text.
    text = r.recognize_google(audio_data)
    print('Speech-to-Text conversion done.\n-------------------------------------------\nOutput:')
    print(text+'\n')