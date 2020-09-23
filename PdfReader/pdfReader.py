import os
import PyPDF2    #reads a pdf book
import pyttsx3  #library for Text-to-speech conversion
import sys

def speak(text):
    speaker = pyttsx3.init()
    
    voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"   
    #this changes the voice to female "MicroSoft Zira"
    #for more change Zira to david or some other find it on the internet
    
    speaker.setProperty('voice', voice_id)
    
    engine.setProperty("rate", 178)
    #this sets the TTS to 178 words per minute(change as you desire)
    
    speaker.say(text)
    speaker.runAndWait()

arr = os.listdir('F:\\Final Year Project/voiceAssistant/books')
speak("which book do you want to read")
speak("here are the list of books available")
print(*arr, sep="\n")
key = input("Enter the keyword for the book you wish to read")

for file_name in arr:
    if key in file_name:
        speak(file_name)
        absolute_path = os.path.abspath('books/'+ file_name)
        book = open(str(absolute_path),'rb')
        pdf_reader = PyPDF2.PdfFileReader(book)
        pages = pdf_reader.numPages
        speak("Enter page number")
        page_number = input("Enter page number:")
        for num in range(int(page_number),pages):
            page = pdf_reader.getPage(num)
            text = page.extractText()
            speak(text)
    else:
        speak("book not found")
            sys.exit()
