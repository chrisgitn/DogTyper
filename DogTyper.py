import random
import string
from hugchat import hugchat
from hugchat.login import Login
import requests
import json
import webbrowser

def dog():
    f = r"https://random.dog/woof.json"
    page = requests.get(f)
    data = json.loads(page.text)
    webbrowser.open(data["url"])
dog()

# Hugging chat login
sign = Login('YOURUSERNAMEHERE', 'YOURPASSWORDHERE') # Hugging chat login details
cookies = sign.login()
cookie_path_dir = "./cookies"

# Hugging chat bot
dogChat = hugchat.ChatBot(cookies=cookies.get_dict())
query_result = dogChat.chat("Write a creative description of a dog that has a job consisting of typing on a typewriter, in this format:Name:____ Age:____ Description:____ ")
print(query_result)

# Dog Typewriting
text = input('Your Text:')
mtext = ''
textLength = len(text) + 1
allLetter = string.ascii_lowercase + ' '

while textLength > 1:
    mtext = mtext + allLetter[random.randrange(0,27)]
    textLength -= 1

i = 0
chance = 0
ch = 27
for x in mtext:
    if x == text[i]:
        print(f'yes, it was {x}')
        chance += 1
    i += 1
ch = ch**chance

print(mtext)
if (1/ch)*100 == 100:
    print('The dog did not match any characters')
else:
    print(f'The chance of this dog matching {chance} characters is {(1/ch)*100}%')