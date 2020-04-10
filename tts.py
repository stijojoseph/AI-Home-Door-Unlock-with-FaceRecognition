import pyttsx3
engine = pyttsx3.init() # object creation
def speakout(k):

 rate = engine.getProperty('rate')   # getting details of current speaking rate
 print (rate)                        #printing current voice rate
 engine.setProperty('rate', 135)     # setting up new voice rate



 volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
 print (volume)                          #printing current volume level
 engine.setProperty('volume',5.0)    # setting up volume level  between 0 and 1

 voices = engine.getProperty('voices')       #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
 engine.setProperty('voice', voices[12].id)   #changing index, changes voices. 1 for female

 
 engine.say(k)
 engine.runAndWait()
 print("hello")
 engine.stop()
