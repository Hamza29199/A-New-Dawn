import googletrans
from googletrans import Translator


t=Translator()    #Creating a google translate object here for the translation

print("Hey there! Let's get moombling.")
print("")

print("Here are the language codes")
print("")
print("")
print(googletrans.LANGUAGES)  #this prints out all the lang codes (en=English, ur=urdu, etc.) so that user knows his/her options
print("")
print("")

from twilio.rest import Client as twi   #importing this to allow us to create a Twilio Client object capable of sending messages between phone numbers

acc_sid="ACd0a78b68d5b0a35520c69fc86edc1619"

auth_token="e96a372d2299459775073e578a9cd4fd"

client=twi(acc_sid,auth_token)      #Client object called client created here


msg=input("Enter your message: ")
trans_code=input('Enter your translation code: ')

trans_msg=t.translate(text=str(msg),dest=str(trans_code))     #translates message according to message and destination language code entered by user

#the translated message is cleaned by removing unnecessary symbols before sending it to specified number

trans=str(trans_msg)

trans=trans.replace("Translated","")
trans=trans.replace("src=en","")
trans=trans.replace(", dest=","")
trans=trans.replace(", text=","")
trans=trans.replace(str(trans_code),"")

trans=trans.replace(str(msg),"")
trans=trans.replace(", pronunciation=","")
trans=trans.replace("None","")
trans=trans.replace("src", "")

    
print(trans)

#any message placed in the body field gets sent to the number in the "to" field (that number has to be registered in your Twilio account)
message=client.messages.create(to="any_registered_number",
                              from_="+18133286584",
                              body=trans)


print(message.sid) #this getting printed is a confirmation that the message has been sent

