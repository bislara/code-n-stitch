import speech_recognition as sr
filename = input("Enter filename (without extenstion): ")+".wav"

# Initializing speech recognizer
r = sr.Recognizer()

# Opening the file
with sr.AudioFile(filename) as source:
    # Loading audio data onto memory
    audio_data = r.record(source)
    print('Audio data successfully loaded from ' + filename + ' to memory.\nConverting speech to text...')
    # Recognizing speech and converting to text.
    
    try:
        text = r.recognize_google(audio_data)
        print('Speech-to-Text conversion done.\n------------------------------------------------\nOutput:')
        print(text+'\n')
    except:
        print('Couldn\'t establish connection with Google server.')
        print('---------------------------------------------------\nSpeech-to-Text conversion failed. Please try again.')
    