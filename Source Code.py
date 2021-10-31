import speech_recognition as sr 
import pyttsx3 
import emoji

print("Choose Mode: 1. Speech to Text 2. Text to Speech")
mode = int(input())

if (mode == 1): 
    def switchLanguage(userLang):
        switcher = {
            1: "en-IN",
            2: "hi-IN",
            3: "fr-FR",
            4: "mr-IN",
            5: "es-ES"
        }
        return switcher.get(userLang, 0)

    def getEmoji(text_to_emoji):  
        emoji = {
            'hello': '\U0001F604',
            'wow': '\U0001F929',
            'lol': '\U0001F923',
            'quiet': '\U0001F92B',
            'cheers': '\U0001F37B',
            'think': '\U0001F914',
            'yes': '\U0001F44D',
            'no': '\U0001F44E',
            'morning': '\U0001F304',
            'night': '\U0001F634',
            'love': '\U00002764',
            'party': '\U0001F973',
            'yummy': '\U0001F924',
            'nice': '\U0001F44C',
            'bye': '\U0001F44B'
        }
        return emoji.get(text_to_emoji)

    r = sr.Recognizer() 
      
    try:
                
        with sr.Microphone() as source2:
                    
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print('Select from the following languages:\n1. English \n2. Hindi \n3. French \n4. Marathi \n5. Spanish')
            userLang = int(input())

            print("Choose convertion option: \n1. Text without Emojis \n2. Text with Emojis \n3. Notes mode")
            type = int(input())
                    
            if type == 1:
                print("Listening..")
                audio_input = r.listen(source2)
                myText = r.recognize_google(audio_input, language = switchLanguage(userLang))
                myText = myText.capitalize() 
                print("Did you say: " + myText)
            elif type == 2:
                    print("Listening..")
                    audio_input = r.listen(source2)
                    myText = r.recognize_google(audio_input, language = switchLanguage(userLang))
                    myText = myText.lower() 
                    text_to_emoji = myText.split()
                    length = len(text_to_emoji)

                    for i in range(length):
                        code = getEmoji(text_to_emoji[i])
                        if(code):
                            x = emoji.emojize(code)
                            print(text_to_emoji[i] + x )
                        else:
                            print(text_to_emoji[i])
                
            if type == 3:
                print("Listening..")
                while True:
                    audio_input = r.listen(source2)
                    myText = r.recognize_google(audio_input, language = switchLanguage(userLang))
                    myText = myText.capitalize() 
                    
                    if(myText == 'Stop audio'):
                        print("Stopped!")
                        break
                    print(myText)
                    save = open("Auto Saved Notes.txt", "a") 
                    save.write("\n" + myText)
                    save.close()

    except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
                
    except sr.UnknownValueError:
            print("Unable to understand the input")

elif (mode == 2):  
    file = open("myTextFile.txt", "r")    
    engine = pyttsx3.init()
    for x in file:
        engine.say(file.read()) 
    file.close()
    engine.runAndWait()
