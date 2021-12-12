import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)

if __name__=='__main__':
    speak("News for Today")
    url="https://newsapi.org/v2/top-headlines?country=in&apiKey=c9f8e0ff652b4dc48d16f32abf4ae07e"
    news=requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    for article in arts:
        speak(article['title'])
        print(article['title'])
        speak("moving on next news")



# def speak(str):
#     from win32com.client import Dispatch
#     speak = Dispatch("SAPI.SpVoice")
#     speak.Speak(str)

# if __name__=='__main__':
#     # speak("Tuch nav kay ahe")
#     speak("Can you tell your name ")
#     a=input("Enter your name : ")
#     speak(f"{a} your are a nice person")
#     # speak(f"{a} tu khup chagla ahes")
#     # speak("ajun kay madat karu")
#     speak("how can i help you")
