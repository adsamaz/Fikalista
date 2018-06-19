import requests
import json
import datetime
import time

# GET
# r = requests.get(url)

# GET with params in URL
# r = requests.get(url, params=payload)

#url = 'http://chatt.sfa.se/hooks/4o1sdns6qj8z7b37xtfmrgwxuy'
url = 'http://localhost:8065/hooks/zp9hbdpunirdpr1dqgjbiud8ow'
currentNum = 6      #Change this number on restart
now = datetime.datetime.now()
wednesdayDone = False
fridayDone = False

while True:
    now = datetime.datetime.now()
    #print("HEJ")
    if now.weekday() == 1 and now.strftime("%H:%M") == "11:19" and not wednesdayDone:  # On wednesday 09:00, print the current fikaperson
        file = open("namnlista", "r", encoding="utf-8-sig")
        names = file.readlines()
        file.close()

        currentName = names[currentNum]

        payload = {'Content-Type': 'application/json', 'text': '<!all> ' + currentName + ' är fikaansvarig denna vecka :cake: Hela fikalistan finns <http://confluence.sfa.se/display/VER/Fikalista/|här> '}
        request = requests.post(url, data=json.dumps(payload))  #Send message to Mattermost
        print("Monday message sent: " + request.text)
        wednesdayDone = True
        fridayDone = False


    elif now.weekday() == 4 and now.strftime("%H:%M") == "14:00" and not fridayDone:  # On friday 14:00, print the upcomming fikaperson
        file = open("namnlista", "r", encoding="utf-8-sig")
        names = file.readlines()
        file.close()
        if currentNum >= len(names) - 1:    #Reset counter if previous preson was the last one in file
            currentNum = 0
        else:
            currentNum += 1

        currentName = names[currentNum]     #Fikapersonen for next week


        payload = {'Content-Type': 'application/json', 'text': currentName + ' är fikaansvarig nästa vecka :cake: Hela fikalistan finns <http://confluence.sfa.se/display/VER/Fikalista/|här> '}
        request = requests.post(url, data=json.dumps(payload))  #Send message   to Mattermost
        print("Friday message sent: " + request.text)
        wednesdayDone = False
        fridayDone = True

    time.sleep(60)
