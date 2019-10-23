'''
Offenses to input:aggravated-assault,all-other-larceny,all-other-offenses,animal-cruelty,arson,assisting-or-promoting-prostitution,bad-checks,betting,bribery,burglary-breaking-and-entering,
counterfeiting-forgery,credit-card-automated-teller-machine-fraud,destruction-damage-vandalism-of-property,driving-under-the-influence,drug-equipment-violations,drug-violations,
drunkenness,embezzlement,extortion-blackmail,false-pretenses-swindle-confidence-game,fondling,gambling-equipment-violation,hacking-computer-invasion,
human-trafficking-commerical-sex-acts,human-trafficking-commerical-involuntary-servitude,identity-theft,impersonation,incest,intimidation,justifiable-homicide,kidnapping-abduction,
motor-vehicle-theft,murder-and-nonnegligent-manslaughter,negligent-manslaughter,operating-promoting-assiting-gambling,curfew-loitering-vagrancy-violations,peeping-tom,
pocket-picking,pornography-obscence-material,prostitution,purchasing-prostitution,purse-snatching,rape,robbery,sexual-assult-with-an-object,sex-offenses-non-forcible,shoplifting,
simple-assault,sodomy,sports-tampering,statutory-rape,stolen-property-offenses,theft-from-building,theft-from-coin-operated-machine-or-device,theft-from-motor-vehicle,
theft-of-motor-vehicle-parts-or-accessories,theft-from-motor-vehicle,weapon-law-violation,welfare-fraud,wire-fraud,not-specified,liquor-law-violations,crime-against-person,
crime-against-property,crime-against-society,assault-offenses,homicide-offenses,human-trafficking-offenses,sex-offenses,sex-offenses-non-forcible, fraud-offenses,larceny-theft-offenses,
drugs-narcotic-offenses,gambling-offenses,prostitution-offenses,all-offenses

'''

import requests
from tkinter import *

def writeHTML(data):
        myfile = open("myapi.html","w")
        myfile.write("<h1>" + e1.get() + " count in " + e2.get() + "</h1>")
        myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for an organized format.</p>")
        myfile.write(data)
        myfile.close()

def main():
        try:
                url = "https://api.usa.gov/crime/fbi/sapi/api/data/nibrs/" + e1.get() + "/offense/states/" + e2.get() + "/count/?api_key=2T0E0qUIFaisgBA2tagaheybrMuQ10sJabAqyYl1"
                print(url)

                response = requests.get(url)

                if (response.status_code == 200):
                        data = response.content
                        data_as_str = data.decode()
                        writeHTML(data_as_str)
                        datajson = response.json()

                else:
                    data = "An error has occurred."
                    writeHTML(data)

        except:
            print("An error has occurred.")

win = Tk()
win.geometry('500x500')
win.title('Enter an offense and a state abbreviation.')

e1 = Entry(win)
e1.grid(row=0,column=0)
e2 = Entry(win)
e2.grid(row=0,column=1)
butt1 = Button(win, text="Go", command=main)
butt1.grid(row=1, column=1)
