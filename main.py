#MAIN DECLARATION

import twitter, time, sys
import telegram

api = twitter.Api(consumer_key='c5RCiZmC2yl6giIqtovEFYOdV', consumer_secret='cxw1C9fxFhbyizCgyymcNXTgfIZ631Xfj0DYjjr4eNKK5d3F9D', access_token_key='1937280930-Mz5dD3z3AfL1YH3kF7K7DVK1bvFtIJdRnrArWMP', access_token_secret='K32tCxA356Rpd6yCnWA8Bw8f6LohwPyNY2AcM8Yfy80R4')

bot = telegram.Bot(token="144762386:AAGA1ElcWoFvE-MEL3zT7DaYaZCUT3NKbnI") #bot name jarvis


id = 179042557

#functions

def getMyTimeLine():
    return api.GetHomeTimeline(count=1)

def textMessage(name, text1):
    Name = "*"+name+"*"
    final = Name+" - "+text1
    bot.sendMessage(chat_id=id, text=final, parse_mode=telegram.ParseMode.MARKDOWN)

NAME_HOLDER = ""
TEXT_HOLDER = ""
NAME_HOLDER_t = ""
TEXT_HOLDER_t = ""


while 1:
    try:
        #to catch a tweet
        ins = getMyTimeLine()

        #There parms will hold out data

        for s in ins:
            print s.user.name
            NAME_HOLDER = s.user.name
            print s.text
            TEXT_HOLDER = s.text

        if (TEXT_HOLDER != TEXT_HOLDER_t):
            textMessage(NAME_HOLDER, TEXT_HOLDER)

        NAME_HOLDER_t = NAME_HOLDER
        TEXT_HOLDER_t = TEXT_HOLDER
        time.sleep(300)

    except:
        print "reloop"
        time.sleep(300)
