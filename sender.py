from microbit import *
import radio
import random

broadcastPower=""
timeBetweenBroadcasts=100 #How long to wait (in MS) between broadcasts. Decreasing this number will make the system more responsive at the expense of battery life
numberOfLandmarks=6 #How many different landmarks does the root contain?

radio.on()

def selectBroadcastPower():
 display.clear()
 i=0
 button_a.was_pressed()
 button_b.was_pressed()
 while True:
  display.show(str(i), wait=False)
  if button_b.was_pressed(): return i
  if button_a.was_pressed():
   i=i+1
   if i > 7: i=0
   display.clear()
   print("Showing %i" % i)

def selectLandmark():
 display.clear()
 print("Select a landmark:\n0")
 i=1
 button_a.was_pressed()
 button_b.was_pressed()
 while True:
  display.show(str(i), delay=100, wait=False)
  if button_b.was_pressed(): return i
  if button_a.was_pressed():
   i=i+1
   if i > numberOfLandmarks: i=0
   display.clear()
   print(i)

def startBroadcasting(broadcastPower :int, objectID :int):
 random.seed(running_time())
 uniqueID=str(random.randint(1000,9999))
 stringToSend=str(uniqueID)+":"+str(objectID+1) #Do the +1 because the receiver starts at 1
 messageToPrint="I am broadcasting "+objectIDs[objectID]+", at a power level of "+str(broadcastPower)+", with a unique ID of "+str(uniqueID)+"."
 print(messageToPrint)
 display.scroll(messageToPrint, delay=100, wait=True)
 sleep(timeBetweenBroadcasts)
 display.clear()
 radio.config(power=broadcastPower, length=16)
 while True:
  radio.send(stringToSend)
  sleep(750)


button_a.was_pressed()
button_b.was_pressed()
print("In main")
while True:
 display.scroll("Select my broadcast power using button a then press b to continue.", delay=100, wait=False)
 while broadcastPower == "":
  if button_a.was_pressed():
   print("Select broadcast power")
   broadcastPower=selectBroadcastPower()
 display.clear()
 display.scroll("Select the landmark that I should represent using button a then press b to continue", delay=100, wait=False)
 while landmarkID == "":
  if button_a.was_pressed():
   print("Select landmark")
   landmarkID=selectObjectID()
 display.clear()
 startBroadcasting(broadcastPower, landmarkID)